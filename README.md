# Grub Grabber
University of Glasgow - WAD2 Group Project

Grub Grabber is a web application designed to give users (anonymous or signed in) easy-to-access lunch destination suggestions. The suggestions include places like cafes, restaurants, bars that serve food, as well as cheaper daily options such as supermarkets, and convenience stores.

Grub Grabber makes use of the [Google Maps Javascript API v3](https://developers.google.com/maps/documentation/javascript/) to provide details about places.

See the Design folder for design documentation including wireframes, database structure, and user personas.

## Installation

1. Set up new virtual environment.
2. Clone repository.
3. Install project dependencies: `pip install -r requirements.txt`
4. Create the database file: `python manage.py migrate` or `./manage.py migrate`

## Usage

1. (Optional) Populate database with some fake users: `python populate_grubgrabber.py` or `./populate_grubgrabber.py`
2. Run the Django development server with `python manage.py runserver` or `./manage.py runserver`
3. Access site at `127.0.0.1:8000` by default.

If the population script has been run, then a test user will exist with username `test` and password `test`.

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
- Isaac Jordan - https://github.com/Sheepzez
- Ben Jackson - https://github.com/ExogenesisBen
- Callum Nixon -https://github.com/2072704N
- Jack Croal - https://github.com/2062685c

## License

View the `LICENSE` file in the root of the repository.
