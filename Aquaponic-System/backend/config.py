class Config:
    """
    Config class for Flask application settings.

    Attributes:
        SECRET_KEY (str): The secret key for the Flask app.
        DEBUG (bool): Enable or disable debug mode.
        TESTING (bool): Enable or disable testing mode.
        SESSION_COOKIE_SECURE (bool): Set to True for secure session cookies in production.
        PERMANENT_SESSION_LIFETIME (int): Session lifetime in seconds (1 hour in this example).

        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable modification tracking for SQLAlchemy.
    """

    # Flask App Configurations
    SECRET_KEY = "My App"
    DEBUG = True  # Enable debugging during development. Set to False in production.
    TESTING = False
    SESSION_COOKIE_SECURE = True  # Set to True for secure session cookies in production
    PERMANENT_SESSION_LIFETIME = 3600  # Session lifetime in seconds (1 hour in this example)

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
