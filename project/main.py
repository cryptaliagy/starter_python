from absl import app
from absl import flags


FLAGS = flags.FLAGS


def main(argv):
    del argv


def entry_point():
    app.run(main)


if __name__ == "__main__":
    entry_point()
