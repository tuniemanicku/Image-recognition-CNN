from pinterest_dl import PinterestDL

def main():

    # Search for train images
    images = PinterestDL.with_api().search_and_download(
        query="memes",
        output_dir="memes",
        num=150
    )
    # Search for test images
    images = PinterestDL.with_api().search_and_download(
        query="funny_memes",
        output_dir="test_memes",
        num=30
    )

if __name__ == "__main___":
    main()