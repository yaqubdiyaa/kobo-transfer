import argparse
import json
import sys

from helpers.config import Config
from transfer.media import get_media, del_media
from transfer.xml import (
    get_src_submissions_xml,
    get_submission_edit_data,
    print_stats,
    transfer_submissions,
)
from xls_transfer.xlsx_kobo import general_xls_to_xml

def main(
    warnings,
    xtransfer,
    excel_file,
    limit,
    last_failed=False,
    keep_media=False,
    regenerate=False,
    quiet=False,
    validate=True,
    config_file=None,
):

    config = Config(config_file=config_file, validate=validate)
    config_src = config.src

    if not xtransfer:
        print('📸 Getting all submission media', end=' ', flush=True)
        get_media()

    xml_url_src = config_src['xml_url'] + f'?limit={limit}'

    if last_failed and config.last_failed_uuids:
        xml_url_src += f'&query={json.dumps(config.data_query)}'

    all_results = []

    submission_edit_data = get_submission_edit_data()

    print('📨 Transferring submission data')

    def transfer(all_results, url=None):
        if (xtransfer):
            parsed_xml = general_xls_to_xml(excel_file, submission_edit_data, warnings)
        else:
            parsed_xml = get_src_submissions_xml(xml_url=url)

        submissions = parsed_xml.findall(f'results/{config_src["asset_uid"]}')
        next_ = parsed_xml.find('next').text
       
        """results = transfer_submissions(
            submissions,
            submission_edit_data,
            quiet=quiet,
            regenerate=regenerate,
        )
        all_results += results"""
   
        if next_ != 'None' and next_ is not None:
            transfer(all_results, next_)
        
    transfer(all_results, xml_url_src)
    
    if not xtransfer:
        if not keep_media:
            del_media()

    print('✨ Done')
    print_stats(all_results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A CLI tool to transfer submissions between projects with identical XLSForms.'
    )

    parser.add_argument( 
        '--print-warnings',
        '-w',
        default = False,
        action = 'store_true', 
        help='Print warnings if questions in Kobo form do not match XLS form.', 
    )

    parser.add_argument( 
        '--google-transfer',
        '-gt',
        default = False,
        action = 'store_true', 
        help='Complete transfer from Google Form data to Kobo project.', 
    )
    parser.add_argument( 
        '--excel-transfer',
        '-xt',
        default = False,
        action = 'store_true', 
        help='Complete transfer from any xlsx form to Kobo project.', 
    )
    parser.add_argument( 
        '--excel-file',
        '-ef', 
        help='Excel file path for data to upload', 
    )
    parser.add_argument(
        '--limit',
        '-l',
        default=30000,
        type=int,
        help='Number of submissions included in each batch for download and upload.',
    )
    parser.add_argument(
        '--last-failed',
        '-lf',
        default=False,
        action='store_true',
        help='Run transfer again with only last failed submissions.',
    )
    parser.add_argument(
        '--config-file',
        '-c',
        default='config.json',
        type=str,
        help='Location of config file.',
    )
    parser.add_argument(
        '--regenerate-uuids',
        '-R',
        default=False,
        action='store_true',
        help='Regenerate submission UUIDs.',
    )
    parser.add_argument(
        '--no-validate',
        '-N',
        default=False,
        action='store_true',
        help='Skip validation of config file.',
    )
    parser.add_argument(
        '--keep-media',
        '-k',
        default=False,
        action='store_true',
        help='Keep submission attachments rather than cleaning up after transfer.',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        default=False,
        action='store_true',
        help='Suppress stdout',
    )
    args = parser.parse_args()

    if (args.excel_transfer and not args.excel_file) or (args.google_transfer and not args.excel_file):
        parser.error("If --excel-transfer (-xt) or --google-transfer (-gt) is passed, --excel-file (-xt) is required.")

    try:
        main(
            warnings = args.print_warnings,
            xtransfer = args.excel_transfer,
            excel_file=args.excel_file,
            limit=args.limit,
            last_failed=args.last_failed,
            regenerate=args.regenerate_uuids,
            keep_media=args.keep_media,
            quiet=args.quiet,
            validate=not args.no_validate,
            config_file=args.config_file,
        )
    
    except KeyboardInterrupt:
        print('🛑 Stopping run')
        # Do something here so we can pick up again where this leaves off
        sys.exit()


