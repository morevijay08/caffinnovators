"""Illustrative interest-reflection questions; not a psychometric diagnosis."""
QUESTIONS = [
 {"id":"q1","prompt":"Which activity would you enjoy most on a free afternoon?","options":[{"id":"a","text":"Build a simple app or gadget","signals":["technology","problem_solving"]},{"id":"b","text":"Draw a poster or design an outfit","signals":["design","arts"]},{"id":"c","text":"Organise a community event","signals":["helping_people","business"]}]},
 {"id":"q2","prompt":"Which school project sounds most exciting?","options":[{"id":"a","text":"Investigate an experiment","signals":["science","mathematics"]},{"id":"b","text":"Write a story or present an idea","signals":["writing","arts"]},{"id":"c","text":"Plan a sports tournament","signals":["sports","business"]}]},
 {"id":"q3","prompt":"What kind of problem do you enjoy solving?","options":[{"id":"a","text":"A tricky puzzle with patterns","signals":["mathematics","problem_solving"]},{"id":"b","text":"Make something easier to use","signals":["design","technology"]},{"id":"c","text":"Help friends understand a challenge","signals":["helping_people","writing"]}]},
 {"id":"q4","prompt":"If you joined a club, which would you choose?","options":[{"id":"a","text":"Robotics and coding","signals":["technology","science"]},{"id":"b","text":"Nature and sustainability","signals":["environment","science"]},{"id":"c","text":"Drama and creative writing","signals":["arts","writing"]}]},
 {"id":"q5","prompt":"Which outcome would make you proudest?","options":[{"id":"a","text":"Creating a tool people can use","signals":["technology","design"]},{"id":"b","text":"Making a positive difference to people","signals":["helping_people","environment"]},{"id":"c","text":"Turning an idea into a small venture","signals":["business","problem_solving"]}]},
 {"id":"q6","prompt":"What would you like to learn more about?","options":[{"id":"a","text":"How numbers explain the world","signals":["mathematics","science"]},{"id":"b","text":"How stories and images influence people","signals":["writing","arts"]},{"id":"c","text":"How teams train and improve","signals":["sports","helping_people"]}]}
]

# Alternate prompts keep repeat assessments fresh without changing the scoring categories.
# Each assessment uses one question per original slot (q1..q6).
ALTERNATE_QUESTIONS = [
 {"id":"q1b","prompt":"What would you most enjoy doing during a weekend workshop?","options":[{"id":"a","text":"Program a small game","signals":["technology","problem_solving"]},{"id":"b","text":"Create a digital illustration","signals":["design","arts"]},{"id":"c","text":"Plan a fundraiser with friends","signals":["helping_people","business"]}]},
 {"id":"q2b","prompt":"Which class challenge would you volunteer for?","options":[{"id":"a","text":"Test a science hypothesis","signals":["science","mathematics"]},{"id":"b","text":"Write and perform a short play","signals":["writing","arts"]},{"id":"c","text":"Coordinate an inter-school sports day","signals":["sports","business"]}]},
 {"id":"q3b","prompt":"When a team gets stuck, what would you rather do?","options":[{"id":"a","text":"Find a logical pattern in the problem","signals":["mathematics","problem_solving"]},{"id":"b","text":"Sketch a simpler design for the solution","signals":["design","technology"]},{"id":"c","text":"Explain the issue clearly to everyone","signals":["helping_people","writing"]}]},
 {"id":"q4b","prompt":"Which student event would you sign up for?","options":[{"id":"a","text":"Build a small robot","signals":["technology","science"]},{"id":"b","text":"Plant trees and track local biodiversity","signals":["environment","science"]},{"id":"c","text":"Create a theatre production","signals":["arts","writing"]}]},
 {"id":"q5b","prompt":"What sort of achievement would excite you?","options":[{"id":"a","text":"Designing a useful phone feature","signals":["technology","design"]},{"id":"b","text":"Improving a local park for everyone","signals":["helping_people","environment"]},{"id":"c","text":"Launching a student-run product stall","signals":["business","problem_solving"]}]},
 {"id":"q6b","prompt":"Which video series would you watch first?","options":[{"id":"a","text":"Everyday maths and physics explained","signals":["mathematics","science"]},{"id":"b","text":"Making comics and telling visual stories","signals":["writing","arts"]},{"id":"c","text":"How athletes train as a team","signals":["sports","helping_people"]}]},
 {"id":"q1c","prompt":"If you could join one project for a month, what would it be?","options":[{"id":"a","text":"Build a website for a local cause","signals":["technology","problem_solving"]},{"id":"b","text":"Design a mural with classmates","signals":["design","arts"]},{"id":"c","text":"Organise a community celebration","signals":["helping_people","business"]}]},
 {"id":"q2c","prompt":"What would you present at a school exhibition?","options":[{"id":"a","text":"A simple chemistry demonstration","signals":["science","mathematics"]},{"id":"b","text":"An original poem and artwork","signals":["writing","arts"]},{"id":"c","text":"A plan for a school sports league","signals":["sports","business"]}]},
 {"id":"q3c","prompt":"How would you prefer to improve a school activity?","options":[{"id":"a","text":"Analyse results and spot patterns","signals":["mathematics","problem_solving"]},{"id":"b","text":"Redesign the instructions and layout","signals":["design","technology"]},{"id":"c","text":"Talk to students and write a clear guide","signals":["helping_people","writing"]}]},
 {"id":"q4c","prompt":"Which after-school programme interests you?","options":[{"id":"a","text":"Inventing with electronics","signals":["technology","science"]},{"id":"b","text":"Water conservation fieldwork","signals":["environment","science"]},{"id":"c","text":"Creative storytelling club","signals":["arts","writing"]}]},
 {"id":"q5c","prompt":"Which project result would satisfy you most?","options":[{"id":"a","text":"A beautifully designed working tool","signals":["technology","design"]},{"id":"b","text":"A cleaner neighbourhood with happier residents","signals":["helping_people","environment"]},{"id":"c","text":"A clever solution that earns money for a cause","signals":["business","problem_solving"]}]},
 {"id":"q6c","prompt":"What would you research just for fun?","options":[{"id":"a","text":"Why mathematical patterns appear in nature","signals":["mathematics","science"]},{"id":"b","text":"How illustrations make stories memorable","signals":["writing","arts"]},{"id":"c","text":"How sports teams support each other","signals":["sports","helping_people"]}]}
]
QUESTION_SETS = [QUESTIONS, ALTERNATE_QUESTIONS[:6], ALTERNATE_QUESTIONS[6:]]
ALL_QUESTIONS = [question for group in QUESTION_SETS for question in group]

# Profile-aware question themes. Each theme is asked in six distinct ways, with
# balanced options that let the learner express *which part* they enjoy.
INTEREST_THEMES = {
 "technology": ("building digital tools", "code a useful app", "design a clear interface", "help someone learn a new device"),
 "science": ("investigating scientific ideas", "test a hypothesis", "draw a clear experiment diagram", "explain findings to classmates"),
 "design": ("creating a new product", "prototype a useful feature", "sketch its visual style", "learn what people need"),
 "writing": ("telling a compelling story", "research facts carefully", "create an illustrated story", "share a message with a community"),
 "business": ("running a small enterprise", "calculate a product budget", "design a brand identity", "help customers solve problems"),
 "helping_people": ("supporting other people", "develop a practical support tool", "make friendly visual instructions", "listen to someone’s concerns"),
 "environment": ("protecting the environment", "measure waste or water use", "design a recycling poster", "bring neighbours together"),
 "arts": ("creating an art project", "experiment with creative technology", "develop a visual concept", "make an artwork with a social message"),
 "mathematics": ("exploring mathematical patterns", "solve a challenging logic puzzle", "visualise patterns in a diagram", "teach a friend a new concept"),
 "sports": ("organising sports activities", "analyse team performance", "design team merchandise", "coach or encourage teammates"),
}
# Each slot uses a new angle while maintaining stable, server-validated choices.
ANGLES = [
 "Imagine a weekend exploring {theme}. Which role sounds most enjoyable?",
 "For a school project about {theme}, what would you choose first?",
 "If you had to solve a challenge involving {theme}, what would you enjoy?",
 "During a club activity about {theme}, where would you contribute?",
 "Which achievement involving {theme} would make you proud?",
 "What skill related to {theme} would you want to try next?",
]
TAILORED_QUESTIONS = []
for key, (theme, analytical, creative, social) in INTEREST_THEMES.items():
    for slot, angle in enumerate(ANGLES):
        TAILORED_QUESTIONS.append({
            "id": f"custom_{key}_{slot}",
            "prompt": angle.format(theme=theme),
            "options": [
                {"id":"a","text":analytical.capitalize(),"signals":[key,"problem_solving"]},
                {"id":"b","text":creative.capitalize(),"signals":[key,"design" if key != "design" else "arts"]},
                {"id":"c","text":social.capitalize(),"signals":[key,"helping_people" if key != "helping_people" else "writing"]},
            ],
        })
ALL_QUESTIONS.extend(TAILORED_QUESTIONS)
