""" module doc here """

from arrow import utcnow

from app.util.reddit_util import submit_competition_post

# -------------------------------------------------------------------------------------------------

POST_TEMPLATE = """##Welcome to competition #{comp_num}!

If you're new, please read the entire post before competing. This competition will run until {due_date}
US/Eastern time.

We'll hold (almost) every WCA event weekly. We are not currently holding 4BLD, 5BLD, and MBLD, but
if there is enough interest we will add them. We'll rotate through a list of bonus events every week.

For a streamlined experience, please visit [cubers.io](https://www.cubers.io), a web app is built
specifically for the /r/cubers weekly competition. By logging into [cubers.io](https://www.cubers.io),
you'll benefit from a number of features, including automatic Reddit comment submission,
leaderboards and personal competition history (coming soon)!

If you want to still compete by manually entering your times, please follow the instructions below:

> * For each event, scramble your cube with the scrambles provided. For COLL, perform the algorithm 5 times.
> * Post your results below in the following format, one event per line:
\n\n`**10x10: 0.41** = 0.37, 0.62, 0.23, (0.07), (1.13)`
> * Common mistakes with formatting include adding a space at the beginning of a line, not writing event
names as they appear in this post, and bolding event name and average separately.

---

**Current Bonus Events**:

{curr_bonus_events}

**Bonus Events In The Queue**:

{upcoming_bonus_events}

---

##This Week's Events

{formatted_events_with_scrambles}"""

SCRAMBLE_LINE_TEMPLATE   = '> 1. {}\n\n'
EVENT_NAME_LINE_TEMPLATE = '\n\n**{}:**\n\n'

# -------------------------------------------------------------------------------------------------

def post_competition(comp_title, comp_num, event_data, curr_bonus, upcoming_bonus):
    """ Post the competition to Reddit and return the Reddit ID. """

    due_date = utcnow().to('US/Eastern').format('hh:MM A on dddd, MMMM Do YYYY')

    curr_bonus_events     = '\n\n> * ' + '\n\n> * '.join(curr_bonus)
    upcoming_bonus_events = '\n\n> * ' + '\n\n> * '.join(upcoming_bonus)

    event_section = ''
    for event in event_data:
        if event['name'] == 'COLL':
            event_section += EVENT_NAME_LINE_TEMPLATE.format(event['name'])
            event_section += SCRAMBLE_LINE_TEMPLATE.format(event['scrambles'][0] + ' (5 times)')
            continue
            
        event_section += EVENT_NAME_LINE_TEMPLATE.format(event['name'])
        for scramble in event['scrambles']:
            event_section += SCRAMBLE_LINE_TEMPLATE.format(scramble)

    post_body = POST_TEMPLATE.format(
        due_date = due_date,
        comp_num = comp_num,
        curr_bonus_events = curr_bonus_events,
        upcoming_bonus_events = upcoming_bonus_events,
        formatted_events_with_scrambles = event_section
    )

    new_comp_id = submit_competition_post(comp_title, post_body)
    return new_comp_id