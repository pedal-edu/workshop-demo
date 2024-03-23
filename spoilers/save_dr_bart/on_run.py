"""
This is provided as an example of a much more complicated activity. It's actually meant
to be run in the browser via BlockPy, so I recommend you check out the link in the `problem.md`
file instead. 
"""

from pedal import *

suppress("syntax", "blank_source")

def set_instructions(message):
    """
    This is usually defined in the BlockPy environment, but since we're on the command line
    we have to define it here instead.
    """
    print(message)

# This is a BlockPy feature, not a Pedal feature! You can just hardcode your name for now.
student_name = "Ada Bart"

VIDEO_TEMPLATE = """<iframe width="400" height="300" 
    src="https://www.youtube.com/embed/{}autoplay=1&modestbranding=1&loop=1&controls=1"
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>"""
video = dict(intro="nGhauRdd4VM?",
            exit_false="sGIh9hHSpTo?",
            open_door="oAF607pJn5M?",
            read_method='0zvJuACqt4c?',
            help_function="FYyKLxnS_tY?",
            ghostly_message="eNsxpblpX70?",
            potion_instructions="FZatI4Jsh_Y?",
            treat_function="p8v1vsEOndI?",
            ada_ending="wyzc9dC072g?list=PLAxDths7gxpAqyazaFlQ0vv9NZ8XS0Kol&",
            babbage_ending="xLH9dDtcnqY?list=PLAxDths7gxpBWSQlw1YS4PC211F_hkMqp&",
            pumpkin_ending="2311ZTFY9Ic?list=PLAxDths7gxpDC9cg9Z5IBn1TrFm3lZftK&")
video = {n: VIDEO_TEMPLATE.format(v) for n, v in video.items()}

guide = dict(intro='Make a new variable named `exit` and assign it the value of `True`.',
            open_door="Call the built-in function `open` using the string literal `'door'`. Do not erase old code.",
            read_method="Assign the result of your `open` function to a new variable. Then, call the `read` method on that variable and print the result.",
            help_function="Define a function named `help` that consumes a string (representing the name of a person) and returns a string with a plea for help added.",
            ghostly_message='''
Copy and paste the following line of code into your program:
```python
ghosts = "👻me👻niih👻tot👻opx👻"
```
Then, use string indexing to print out the character at the following indices: 2, 7, and -3.
Note that ghosts are surprisingly fat - they actually take up two characters instead of one!
Make sure you print each of the three characters on its own line.
When you are done, the ghosts will print their secret message!''',
            potion_instructions="""Define a function named `mix` that consume three integers (red, green, and blue) and produces an integer by adding them together.
             You will need to multiply each parameter by a constant; run your code to see the instructor unit tests and deduce the values!""",
            treat_function="""Define a function named `treat` that consume an animal (a string value) and produces whether
            Dr. Bart should `"keep"` the treat, `"give"` the treat, or `"wait"` for a different animal. If the animal is `"ada"`, return `"give"`.
            If the animal is `"pumpkin"` or `"babbage"`, return `"keep"`. Otherwise, return `"wait"`. Of course, I suppose you could give a treat to a different animal instead...""",
            ada_ending="Mission Accomplished! You earned ending #1\n\nYes, I know it's not Halloween right now - but don't we need some spookiness sometimes?",
            babbage_ending="Mission Accomplished! You earned ending #2\n\nYes, I know it's not Halloween right now - but don't we need some spookiness sometimes?",
            pumpkin_ending="Mission Accomplished! You earned ending #3\n\nYes, I know it's not Halloween right now - but don't we need some spookiness sometimes?",)

completed = dict(intro=False,
                 open_door=False,
                 help_function=False,
                 ghostly_message=False,
                 potion_instructions=False,
                 treat_function=False)

# Introduction
if 'exit' in student.data and not callable(student.data['exit']):
    if student.data['exit'] is True:
        completed['intro'] = True
        give_partial("+10%")
    elif student.data['exit'] is False:
        gently(video['exit_false'], label="exit_false", title="Mean Value")
        set_instructions(guide['intro'])
    else:
        set_instructions(guide['intro'])
        gently("You are not assigning the value `True`", label="intro_wrong_value", title="Wrong Value")
else:
    gently(video['intro'], label="missing_exit", title="Let Us Begin")
    set_instructions(guide['intro'])
    
if completed['intro']:
    if "open" not in get_program():
        print('NO ESCAPE! THE EXIT IS DISABLED!')
    if "The door refuses to open." in get_output():
        completed['open_door'] = True
        give_partial("+10%")
    elif find_match('open("door").read'):
        gently("You are not *calling* the `read` method")
    elif find_match("open('door')"):
        gently(video['read_method'], label="missing_read_method", title="Call Read")
        set_instructions(guide['read_method'])
    else:
        message = "<strong>THE EXIT IS DISABLED</strong>\n"
        gently(message+video['open_door'], label="missing_open_door", title="Open the Door")
        set_instructions(guide['open_door'])
        
if completed['open_door']:
    if 'help' in student.data:     
        failed1 = assert_equal(call('help', student_name), f"Please help me {student_name}!", priority='highest')
        failed2 = assert_equal(call('help', 'student'), f"Please help me student!", priority='highest')
        if not failed1 and not failed2:
            completed['help_function'] = True
            give_partial("+10%")
    else:
        ensure_function('help', arity=1, message=video['help_function'])
        set_instructions(guide['help_function'])
        
if completed['help_function']:
    if "m\ni\nx\n" in student.raw_output:
        completed['ghostly_message'] = True
        give_partial("+10%")
    else:
        gently(f"Dr. Bart reached out to {student_name}... but they couldn't hear him.\n"+video['ghostly_message'],label="missing_ghostly_message", title="What's Happening??")
        set_instructions(guide['ghostly_message'])
        
if completed['ghostly_message']:
    set_instructions(guide['potion_instructions'])
    function_missing = ensure_function('mix', arity=3, message=video['potion_instructions'])
    if not function_missing:
        if unit_test('mix',
            [(1, 1, 1), 6],
            [(1, 2, 3), 11],
            [(3, 2, 1), 13],
            [(4, 4, 4), 24],
            [(0, 3, 1), 5],
            [(5, 0, 0), 15],
        ):
            completed['potion_instructions'] = True
            give_partial("+10%")

if completed['potion_instructions']:
    set_instructions(guide['treat_function'])
    function_missing = ensure_function('treat', arity=1, message=video['treat_function'])
    if not function_missing:
        assert_equal(call('treat', 'badger'), 'wait')
        assert_equal(call('treat', 'nothing'), 'wait')
        assert_equal(call('treat', 'ghost'), 'wait')
        pumpkin = call('treat', 'pumpkin')
        babbage = call('treat', 'babbage')
        ada = call('treat', 'ada')
        if (pumpkin, babbage, ada) == ('keep', 'keep', 'give'):
            set_success(message=video["ada_ending"])
            set_instructions(guide['ada_ending'])
        elif (pumpkin, babbage, ada) == ('keep', 'give', 'keep'):
            set_success(message=video["babbage_ending"])
            set_instructions(guide['babbage_ending'])
        elif (pumpkin, babbage, ada) == ('give', 'keep', 'keep'):
            set_success(message=video["pumpkin_ending"])
            set_instructions(guide['pumpkin_ending'])
        elif 'wait' in (pumpkin, babbage, ada):
            gently("Your `treat` function returns `'wait'` for one of the three animals. Remember, it needs to return `'keep'` or `'give'` for the three animals!", label="treat_returning_wait", title="Treat Function Incorrect")
        else:
            gently("Your `treat` function should only return `give` for one animal, and `keep` for two. Double check your conditionals and return values!", label="incorrect_treat", title="Treat Function Incorrect")
