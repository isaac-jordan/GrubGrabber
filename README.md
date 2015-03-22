# Grub Grabber
University of Glasgow - WAD2 Group Project

This application will provide users with personalised recommendations for places to
get food.

See Design folder for the design documentation.

## Installation

1. Set up new virtual environment.
2. Clone repository.
3. Install project dependencies: `pip install -r requirements.txt`
4. Create the database file: `python manage.py migrate` or `./manage.py migrate`

## Usage

1. (Optional) Populate database with some fake users: `python populate_grubgrabber.py` or `./populate_grubgrabber.py`
2. Run the Django development server with `python manage.py runserver` or `./manage.py runserver`
3. Access site at `127.0.0.1:8000` by default.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

Version 1.0: 27th March 2015

## Credits

Main Development Team:
- Isaac Jordan
- Ben Jackson
- Callum Nixon
- Jack Croal

## License

View the `LICENSE` file in the root of the repository.
