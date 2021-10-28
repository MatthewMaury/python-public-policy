import glob
import json


def test_metadata(notebook, file):
    metadata = notebook["metadata"]

    if file == "pandas_crash_course.ipynb":
        # run in Google Colab
        expected_kernel = "Python 3"
    else:
        expected_kernel = "Python [conda env:python-public-policy] *"

    actual_kernel = metadata["kernelspec"]["display_name"]
    assert (
        actual_kernel == expected_kernel
    ), f"Runtime name (`{actual_kernel}`) incorrect for {file}."

    assert metadata["language_info"]["version"].startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert (
            colab_name == file
        ), f"Name in metadata doesn't match filename for {file}."


for file in glob.glob("*.ipynb"):
    print(f"Checking {file}...")
    notebook = json.load(open(file))
    test_metadata(notebook, file)

print("Passed!")
