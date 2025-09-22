

The Website–[https://cdspeccollab.smcm.edu](https://cdspeccollab.smcm.edu)   
The GitHub Repo (2020)–[https://github.com/drsimonread/COSC4012020](https://github.com/drsimonread/COSC4012020)     

Google guidelines on docstrings: [https://google.github.io/styleguide/pyguide.html\#38-comments-and-docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) 

**Style Guide**  
Comments at the top of class should provide a description of the object and its attributes. e.g.  
    class SampleClass:
        """Summary of class here.

        Longer class information...
        Longer class information...

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not. eggs: An integer count of the eggs we have laid.
        """
    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        self. likes_spam = likes_spam
        self.eggs = 0
    def public_method(self):
    """Performs operation blah."""

Comments at the top of the functions should describe what the functions does as well as its parameters   
and what it returns or throws, e.g.  
    def connect_to_next_port(self, minimum: int) -› int:
    """Connects to the next available port.
    
    Args:
        minimum: A port value greater or equal to 1024.
    
    Returns:
        The new minimum port.
    
    Raises:
        onnectionError: If no available port is found.
    """
