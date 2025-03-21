import random
import sys
import numpy as np

import_template = """
from lib.template_solutions.{} import solution as reference_func
global reference_func
"""

references = {
    "1" : "template1_n_largest_numbers",
    "2" : "template2_clamp_values",
    "3" : "template3_snakespeare",
    "4" : "template4_normalization",
    "5" : "template5_bothon"
}

C_RED = '\033[91m'
C_GREEN = '\033[92m'
C_END = '\033[0m'

class SolutionHandler:
    def __init__(self, id, use_numpy=False, **kwargs):
        setup, self.get_args, self.check, self.post_process = {
            "1" : (self.setup_n_largest, self.get_generic, self.check_n_largest, self.post_generic),
            "2" : (self.setup_clamp, self.get_clamp, self.check_clamp, self.post_generic),
            "3" : (self.setup_snakespeare, self.get_generic, self.check_snakespeare, self.post_snakespeare),
            "4" : (self.setup_normalization, self.get_generic, self.check_normalization, self.post_generic),
            "5" : (self.setup_bothon, self.get_generic, self.check_bothon, self.post_generic),
            "999" : (self.setup_dummy, self.get_generic, self.check_dummy, self.post_dummy)
        }[id]
        self.id = id
        self.use_numpy = use_numpy
        self.args = setup(**kwargs)
        self.shuffle_func = {
            False : random.shuffle,
            True : np.random.shuffle
        }[use_numpy]
    
    
    # General methods
    def get_generic(self):
        if self.shuffle:
            self.shuffle_func(self.args[0])
        return tuple(arg.copy() if hasattr(arg, 'copy') else arg for arg in self.args)
    
    def post_generic(self, results):
        return None
    
    def get_reference(self):
        template = import_template.format(references[self.id])
        # Execute import to access reference function
        try:
            exec(template)
        except ImportError as e:
            sys.exit(f"Could not import reference function. Broken import: '{template}'. Error: {e}")
        
        # Temporarily disable shuffling and get reference results
        _shuffle = self.shuffle
        self.shuffle = False
        reference_result = reference_func(*self.get_args())
        self.shuffle = _shuffle
        return reference_result
    
    def conclude(self, match, message):
        if match:
            return True, "".join([C_GREEN, "Results evaluate correctly!", C_END]), message
        else:
            return False, "".join([C_RED, "Results do not match the expected!", C_END]), message
        
        
    # 1 - N largest numbers
    def setup_n_largest(self, length=10000, n=50):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(length)
        else:
            lst = list(range(length))
        return (lst, n)
    
    def check_n_largest(self, result):
        reference_result = self.get_reference()
        match = True
        for a, b in zip(result, reference_result):
            if a != b:
                match = False
                break
        if len(result) != len(reference_result):
            match = False
        message = f"Your result: {result}\nExpected result: {reference_result}"
        return self.conclude(match, message)
            
        
    # 2 - Clamp values
    def setup_clamp(self, size=200):
        self.shuffle = False
        if self.use_numpy:
            matrix = np.random.randint(low=-200, high=500, size=(size, size))
        else:
            matrix = [[random.randint(-200, 500) for _ in range(size)] for _ in range(size)]
        return (matrix,)
    
    def get_clamp(self):
        if self.use_numpy:
            return (self.args[0].copy(),)
        else:
            _matrix = self.args[0]
            return ([row.copy() for row in _matrix],)
        
    def check_clamp(self, results):
        reference_result = self.get_reference()
        result_sum = sum([sum(row) for row in results])
        reference_sum = sum([sum(row) for row in reference_result])
        match = result_sum == reference_sum
        if match:
            message = ""
        else:
            message = f"The sum of your matrix ({result_sum}) does not match the reference value ({reference_sum}).\n"
        
        contains = False
        if self.use_numpy:
            contains = (results > 255).any() or (results < 0).any()
        else:
            class ClampChecker:
                def __init__(self, lower, upper):
                    self.upper = upper
                    self.lower = lower
                def __eq__(self, value):
                    return (value > self.upper) or (value < self.lower)
            clamp_checker = ClampChecker(0, 255)
            for row in results:
                if row.count(clamp_checker):
                    contains = True
                    break
        if contains:
            C_TEXT = C_RED
        else:
            C_TEXT = C_GREEN
        string = "{}Matrix does {}contain numbers < 0 or > 255.{}".format(
            C_TEXT,
            {True : "still ", False : "not "}[contains],
            C_END
        )
        
        return self.conclude(match, message + string)
    
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        with open("./data/sonnets.txt", "r") as fp:
            sonnets = fp.read()
        if self.use_numpy:
            sonnets = np.array(sonnets)
        return (sonnets,)

    def check_snakespeare(self, result):
        reference_result = self.get_reference()
        match = True
        message = ""
        for key in reference_result.keys():
            if not key in result.keys():
                match = False
                message += f"Missing key: word pair {key}\n"
            elif not len(result[key]) == len(reference_result[key]):
                match = False
                for word in result[key]:
                    if word not in reference_result[key]:
                        message += f"List of words following word pair {key} is missing word {word}.\n"
        return self.conclude(match, message)

    def post_snakespeare(self, word_dict):
        w1, w2 = random.choice([word_pair for word_pair in list(word_dict.keys()) if word_pair[0][0].isupper()])
        num_words = 2
        words = [w1, w2]
        while num_words < 10 or w2[-1] != ".":
            try:
                if (w1, w2) in word_dict.keys():
                    w1, w2 = w2, random.choice(word_dict[(w1, w2)])
                else:
                    w1, w2 = random.choice(list(word_dict.keys()))
            except IndexError as e:
                print()
                print()
                print(f"Error! {e}")
                print(w1, w2, word_dict[(w1, w2)])
                break
            words.append(w2)
            num_words += 1
        return "\n".join(["Snakespeare writes:", " ".join(words)])
    
    
    # 4 - Normalization
    def setup_normalization(self, length=10000):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(length)
        else:
            lst = list(range(length))
        return(lst,)

    def check_normalization(self, result):
        reference_result = self.get_reference()
        match = True
        for a, b in zip(result, reference_result):
            if a != b:
                match = False
                break
        if len(result) != len(reference_result):
            match = False
            
        message = f"Sum of your result: {sum(result)}\nExpected sum: {sum(reference_result)}"
        return self.conclude(match, message)
    
    
    # 5 - Bothon
    def setup_bothon(self, E_split=12, E_mass=3, stop_threshold=60):
        self.shuffle = False
        if self.use_numpy:
            initial_state = np.array([8])
        else:
            initial_state = [8]
        return (initial_state, E_split, E_mass, stop_threshold)
    
    def check_bothon(self, result):
        reference_result = self.get_reference()
        match = result == reference_result
        message = f"Number of bothons; your result: {result}\nExpected result: {reference_result}"
        return self.conclude(match, message)
    
    # 999 - Dummy exercise
    def setup_dummy(self):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(10000)
        else:
            lst = list(range(10000))
        n = 100
        return (lst, n)
    
    def check_dummy(self, results):
        pass
    
    def post_dummy(self, results):
        pass


class TestRunHandler(SolutionHandler):
    # General methods
    def post_generic(self, results):
        return f"Your results:\n{results}"
    
    
    # 1 N largest numbers
    def setup_n_largest(self):
        return super().setup_n_largest(length=10, n=3)
    
    
    # 2 - Clamp values
    def setup_clamp(self):
        return super().setup_clamp(size=4)
    
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        sample = 'This text is an example text. This text will hopefully help. For an example is an aid.'
        if self.use_numpy:
            return (np.array(sample),)
        else:
            return (sample,)
    
    def post_snakespeare(self, word_dict):
        print("Word dictionary:")
        for key in word_dict:
            print(key, word_dict[key])
        print()
        return super().post_snakespeare(word_dict)
    
    
    # 4 - Normalization
    def setup_normalization(self):
        return super().setup_normalization(length=10)
    
    
    # 5 - Bothon
    def setup_bothon(self):
        return super().setup_bothon(stop_threshold = 10)