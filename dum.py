import os
import datasets
# should be on datasets

PAIRS = [
    "ar-de",
    "ar-fr",
    "ar-nl",
    "ar-ru",
    "ar-zh",
    "de-fr",
    "de-nl",
    "de-ru",
    "de-zh",
    "fr-nl",
    "fr-ru",
    "fr-zh",
    "nl-ru",
    "nl-zh",
    "ru-zh",
]

for pair in PAIRS:

    dataset = datasets.load_dataset("./datasets/opus_100", language_pair=pair)
    src_tag, tgt_tag = pair.split("-")

    os.chdir("datasets/opus_100/dummy")
    os.system(f"mkdir {pair}")
    os.chdir(pair)
    os.system("mkdir 0.0.0")
    os.chdir("0.0.0")

    BASE = f"datasets/opus_100/dummy/{pair}/0.0.0"
    # COPY_BASE = f"/Users/vasudevgupta/Downloads/mkb/{src}-{tgt}"

    # if "dummy_data.zip" in os.listdir():
    #     os.system("rm -f dummy_data.zip")

    # if "dummy_data" in os.listdir():
    #     os.system("rm -rf dummy_data")

    # os.chdir(BASE)
    os.system("mkdir dummy_data")
    os.chdir("dummy_data")
    # os.system(f"mkdir opus-100-corpus-{pair}-v1.0.tar.gz")
    # os.chdir(f"opus-100-corpus-{pair}-v1.0.tar.gz")
    os.system("mkdir opus-100-corpus")
    os.chdir("opus-100-corpus")
    os.system("mkdir v1.0")
    os.chdir("v1.0")
    os.system("mkdir zero-shot")
    os.chdir("zero-shot")
    os.system(f"mkdir {pair}")
    os.chdir(pair)

    if "train" in dataset:
        os.system(f"touch opus.{pair}-train.{src_tag}")
        os.system(f"touch opus.{pair}-train.{tgt_tag}")

        data = dataset["train"]["translation"][:2]

        s = [d[src_tag] for d in data]
        t = [d[tgt_tag] for d in data]

        with open(f"opus.{pair}-train.{src_tag}", "w") as f1, open(f"opus.{pair}-train.{tgt_tag}", "w") as f2:
            f1.write("\n".join(s))
            f2.write("\n".join(t))

    if "test" in dataset:
        os.system(f"touch opus.{pair}-test.{src_tag}")
        os.system(f"touch opus.{pair}-test.{tgt_tag}")

        data = dataset["test"]["translation"][:2]

        s = [d[src_tag] for d in data]
        t = [d[tgt_tag] for d in data]

        with open(f"opus.{pair}-test.{src_tag}", "w") as f1, open(f"opus.{pair}-test.{tgt_tag}", "w") as f2:
            f1.write("\n".join(s))
            f2.write("\n".join(t))

    if "validation" in dataset:
        os.system(f"touch opus.{pair}-dev.{src_tag}")
        os.system(f"touch opus.{pair}-dev.{tgt_tag}")

        data = dataset["validation"]["translation"][:2]

        s = [d[src_tag] for d in data]
        t = [d[tgt_tag] for d in data]

        with open(f"opus.{pair}-dev.{src_tag}", "w") as f1, open(f"opus.{pair}-dev.{tgt_tag}", "w") as f2:
            f1.write("\n".join(s))
            f2.write("\n".join(t))

    # with open(COPY_BASE+f"/mkb.{src}") as f1, open(COPY_BASE+f"/mkb.{tgt}") as f2:
    #     s = f1.read().split("\n")[:2]
    #     t = f2.read().split("\n")[:2]

    os.chdir(f"/Users/vasudevgupta/desktop/huggingface-datasets/datasets/opus_100/dummy/{pair}/0.0.0")

    os.system(f"zip -r dummy_data.zip dummy_data/")
    os.system("rm -r dummy_data/")
    # os.system("unzip dummy_data.zip")

    os.chdir("/Users/vasudevgupta/desktop/huggingface-datasets")

