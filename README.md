# skaarladder-backend

This project is the backend for the newest, and hopefully last version of [Skaarladder](https://github.com/Josde/Skaarladder).  
  
# Changes from the previous version (when I finish programming this)
- Moved from Django + Jinja2 + HTMX to a more streamlined Django-Rest-Framework API + Vue3 stack.  
- Moved from Pyot to Pulsefire
- Updated to match new S13-14 stuff (name+tag in summoner name, emerald rank)
- Stop using django-rq in favour of manual updates, since periodic tasks were an absolute failure in the previous version and caused a lot of issues.
- Start respecting ratelimits properly
- Dockerize to make deploying not as annoying as it used to be
- Add OpenAPI 
- Hopefully, finish the project with clean code, REST principles and testing in place.

# Things I would love to add
- Hopefully add WebSockets instead of doing dirty hacks with browser reloading?
- Make a profile view so the page doubles as a profile stat tracker
- Add QuestDB for statistics over a long time


# Progress
None, currently. lol.