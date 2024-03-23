# Presentation

If you are watching this at SIGCSE, I recommend not going too far ahead. I'll be going through the slides and code in the presentation.

But if you want to, here's the link to the slides: <https://docs.google.com/presentation/d/1yYSopsVdpwiDtHC5rbnV3id5JXNogXaaihredEHnP1g/edit?usp=sharing>


# Outline

1. Environment Setup
2. Intro
3. Problems
   1. `1_order_out_of`
   2. `2_volume_extraction`
   3. `3_dataclasses`
   4. `4_inputs`
   5. `5_your_own`
   6. `6_gradescope`
4. Verification example
5. Spoilers (!)


# 1. Environment setup

- [ ] Installed [VS Code](https://code.visualstudio.com/) (or Pycharm, if you prefer that)
    - Need to run commands in terminal too
- [ ] Installed [Python 3.7](https://www.python.org/downloads/) or above
    - Make sure it is on your PATH so we can run stuff!
- [ ] Fork and clone **this** Git repository locally
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

# 2. Introduction

1. Open up [intro/validate.py](intro/validate.py) in your editor
2. `cd` to the `intro` folder in your terminal

```sh
pedal feedback validate.py students/correct.py --environment terminal
```

# 3. Problems

I've included 4 actual problems from our courses, covering different places in our curriculum.

1. `1_order_out_of` is a precise practice for string subscripting
2. `2_volume_extraction` is a functional decomposition problem where students are expected to define two functions
3. `3_dataclasses` is an example involving a list of dataclasses, requiring much more complex data
4. `4_inputs` shows how to mock inputs
5. `5_your_own` is a chance to try your own feedback
6. `6_gradescope` is a folder ready to be zipped and uploaded to Gradescope

# 4. Verification

This is an example of how we can "unit test our unit tests". I find that when I make more complicated
Pedal scripts, and start adding a lot of different assertions, I sometimes lose track of things.
If I add a new assertion, how do I know that it won't clobber some other assertion's feedback?

The ``verify`` mode allows you to check a folder full of student submissions against their expected output.
The expected output is stored in easy-to-read `.out` files using an `ini` based format.
The results are shown using the built-in `unittest` module, so changes will be shown as passing and failing
unit tests.

Often, I will first create the expected output automatically, using the `--create_output` flag:

```sh
pedal verify validate.py students/ --create_output
```

Then, as you modify the instructor control script, you can drop the flag:

```sh
pedal verify validate.py students/
```

# 5. Spoilers

Only check this when you have a free moment (and can hear sounds). It's a more complicated
activity that uses Pedal (and some BlockPy) features to make a game.

# 6. Workshop Link

If you are attending SIGCSE 2024, then please fill out the workshop survey:

<https://www.surveymonkey.com/r/sigcse24-workshop-sat>

# 7. Future Engagement

We would love to develop a user community! Check out our Issue tracker and Discussion forum in the 
[Pedal](https://github.com/pedal-edu/pedal) repository.