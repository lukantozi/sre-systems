import argparse
import tempfile
import shutil
import os
import fnmatch
import logging


def get_zip_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("zip", help="zip file to filter")
    args = parser.parse_args()
    zip_file = args.zip
    return zip_file 


def unzip_filter_zip(file):
    removed = []
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.unpack_archive(file, tmpdir)
        logging.info(f"Extracting {file}")
        file_no_zip = os.path.splitext(file)[0]
        tmpdir_pr = os.path.join(tmpdir, file_no_zip)
        write_path = os.path.join(tmpdir_pr, "removed.txt")
        for dirpath, dirnames, filenames in os.walk(tmpdir):
            for dirname in dirnames[:]:
                if fnmatch.fnmatch(dirname, "tmp_*"):
                    bad_dir = os.path.join(dirpath, dirname)
                    rel_path = os.path.relpath(bad_dir, tmpdir_pr)
                    removed.append(f"{rel_path}\n")
                    logging.info(f"Removing directory {rel_path}")
                    shutil.rmtree(bad_dir)
                    dirnames.remove(dirname)
            for file in filenames:
                if fnmatch.fnmatch(file, "*.bak"):
                    file_path = os.path.join(dirpath, file)
                    rel_path = os.path.relpath(file_path, tmpdir_pr)
                    removed.append(f"{rel_path}\n")
                    logging.info(f"Removing file {rel_path}")
                    os.remove(file_path)
        with open(write_path, "w") as f:
            removed.sort()
            logging.info(f"Creating {write_path}")
            f.write("".join(removed))

        logging.info(f"Zipping remaining files into /filtered/{file_no_zip}_filtered.zip")
        shutil.make_archive(f"./filtered/{file_no_zip}_filtered", "zip", tmpdir)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    file = get_zip_file()
    unzip_filter_zip(file)
    logging.info("Filtered successfully")


if __name__ == "__main__":
    main()
