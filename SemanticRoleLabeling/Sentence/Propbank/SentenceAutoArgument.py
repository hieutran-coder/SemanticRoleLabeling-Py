
# Có 2 module được import vào

from abc import abstractmethod

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence

# Class SentenceAutoArgument thì không có Property Và có một abstract method
    # Chữ kí của Abstract method này có seft parameter, và điều này fit với quan điểm trên W3school
class SentenceAutoArgument:

    
    @abstractmethod
    def autoArgument(self, sentence: AnnotatedSentence) -> bool:
        """
        The method should set all the semantic role labels in the sentence. The method assumes that the predicates
        of the sentences were determined previously.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which semantic roles will be determined automatically.
        """
        pass
