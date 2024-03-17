# Presentation

If you are watching this at SIGCSE, I recommend not going too far ahead. I'll be going through the slides and code in the presentation.


# Outline

1. Environment Setup
2. Intro


# Environment setup

- [ ] Installed VS Code (or Pycharm)
    - Would like to be able to run Terminal commands
- [ ] Installed Python 3.7 or above
    - Make sure it is on your PATH so we can run stuff!
- [ ] Fork and clone this Git repository locally
    - Open up the folder in VS Code
- [ ] Make/Activate a Virtual Environment
    - `python -m virtualenv venv`
- [ ] Installed Pedal and other requirements
    - `pip install -r requirements.txt`

To see if Pedal is installed, run `pedal --help` in your terminal. You might need to run
`python -m pedal --help` depending on your PATH, OS, and terminal.

```
usage: pedal [-h] [--alternate_filenames ALTERNATE_FILENAMES] [--output OUTPUT] [--config CONFIG] [--create_output] [--environment {blockpy,gradescope,jupyter,standard,vpl,terminal}] [--instructor_name INSTRUCTOR_NAME]
             [--progsnap_profile PROGSNAP_PROFILE] [--include_scripts INCLUDE_SCRIPTS] [--limit LIMIT] [--resolver {resolve,stats_resolve}] [--ics_direct] [--skip_tifa] [--skip_run]
             [--progsnap_events {run,edit,last,compile}] [--cache CACHE] [--threaded THREADED] [--log_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
             {run,feedback,grade,stats,sandbox,verify,debug} instructor [submissions]

Run instructor control script on student submissions.

positional arguments:
  {run,feedback,grade,stats,sandbox,verify,debug}
                        What kind of Pedal analysis you're running
  instructor            The path to the instructor control script, or multiple scripts.
  submissions           The path to the student submissions. Defaults to a folder named submissions adjacent to the instructor control script.

options:
  -h, --help            show this help message and exit
  --alternate_filenames ALTERNATE_FILENAMES
                        A semicolon separated list of potential filenames to try if the main isn't found.
  --output OUTPUT, -o OUTPUT
                        The output file path for the result. Defaults to stdout.
  --config CONFIG, -c CONFIG
                        Uses the configuration file to get settings.
  --create_output, -m   In verify mode, creates any missing outputs.
  --environment {blockpy,gradescope,jupyter,standard,vpl,terminal}, -e {blockpy,gradescope,jupyter,standard,vpl,terminal}
                        Sets the environment context for this script, which can run special setups and override tools as needed.
  --instructor_name INSTRUCTOR_NAME
                        Sets the name of the instructor file to something more friendly. If not given, then will default to the instructor filename.
  --progsnap_profile PROGSNAP_PROFILE
                        Uses the given profile's default settings for loading in a ProgSnap2 dataset
  --include_scripts INCLUDE_SCRIPTS
                        An optional filter to only include certain scripts
  --limit LIMIT         An optional limit to how many submissions are run. Mostly for testing purposes.
  --resolver {resolve,stats_resolve}
                        Choose a different resolver to use.
  --ics_direct          Give the instructor code directly instead of loading from a file.
  --skip_tifa           Skip using TIFA in the environment
  --skip_run            Skip automatically running student code in the environment
  --progsnap_events {run,edit,last,compile}
                        Choose what level of event to capture from Progsnap event logs.
  --cache CACHE         Use the given directory to hold the cache. You can use "./" to use the current directory.
  --threaded THREADED   Run the instructor script in a separate thread to avoid timeout crashes.
  --log_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level for Pedal.
```

# Introduction

1. Open up [intro/validate.py](intro/validate.py) in your editor
2. `cd` to the `intro` folder in your terminal

```sh
pedal feedback validate.py students/correct.py --environment terminal
```