[![Build Status](https://travis-ci.org/jacobjwebber/software-development.svg?branch=master)](https://travis-ci.org/jacobjwebber/software-development)

# software-development

Software development assignment.

This is a Python web project. It depends on Python and Pip. You will need these installed. Go to https://www.python.org/ if necessary or use package manager (homebrew or dnf/apt-get).

It also depends upon virtualenv. Use pip install virtualenv if necessary.

A build script is included that will automatically install dependencies and run the application on both Mac and linux. To run this go to `src/` dir and run `./build_and_run`. 

On Windows this will need to be done manually, running `pip install -r requirements.txt` from within the `src/` directory, then `python framework.py` from within the `src/app/` directory.

For debugging it may be useful to set the environment variable `FLASK_DEBUG=1`.

This project is open source an is released under the MIT license. See `LICENSE.txt`.
