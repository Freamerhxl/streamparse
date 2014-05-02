from docopt import docopt
from invoke import run

def main():
    """sparse: manage streamparse clusters.

    sparse provides a front-end to streamparse, a framework for creating Python
    projects for running, debugging, and submitting computation topologies against
    real-time streams, using Apache Storm.

    It requires the lein (Clojure build tool) to be on your $PATH, and uses
    lein and Clojure under the hood for JVM interop.

    Usage:
        sparse quickstart <proj_name>
        sparse setup [-e ENV]
        sparse run [-e ENV] [-t TIME]
        sparse debug [-e ENV]
        sparse kill [-e ENV]
        sparse restart [-e ENV]
        sparse attach [-e ENV]
        sparse list [-e ENV]
        sparse submit [-e ENV]
        sparse logs [-e ENV]
        sparse (-h | --help)
        sparse --version

    Options:
        -h --help         Show this screen.
        --version         Show version.
        -e ENV            Set environment; as described in config.json [default: local].
        -t TIME           Time (in milliseconds) to keep cluster running [default: 5000].
        --verbose         Verbose output.
        --debug           Debug output.
    """
    args = docopt(main.__doc__, version="sparse 0.1")
    print args
    if args["run"]:
        print "Running wordcount topology..."
        word_count = "topologies/wordcount.clj"
        run("lein run -s {topology} -t {time}".format(
            topology=word_count, time=args["-t"]))
    elif args["debug"]:
        print "Debugging wordcount topology..."
        run("lein run -s topologies/wordcount.clj")
    elif args["list"]:
        print "invoke tasks:"
        run("invoke -l")
        print
        print "fabric tasks:"
        run("fab -l")
    elif args["setup"]:
        print "Setting up virtualenv on remote cluster..."
        run("fab workers setup_virtualenv")
    elif args["quickstart"]:
        print "Starting a new sparse project..."
        run("echo mkdir -p yourproj ...")


if __name__ == "__main__":
    main()
