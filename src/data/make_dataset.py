import logging
import argparse

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    print(f"reading data from {input_filepath}...")
    print(f"writing data to {output_filepath}...")
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Run data pre-processing")
    parser.add_argument('input_path', type=str, help="input path")
    parser.add_argument('output_path', type=str, help="output path")
    args = parser.parse_args()
    main(args.input_path, args.output_path)
