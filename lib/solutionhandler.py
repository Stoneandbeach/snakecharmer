import random
import numpy as np

class SolutionHandler:
    def __init__(self, id, use_numpy=False, **kwargs):
        setup, self.get_args, self.post_process = {
            "1" : (self.setup_n_largest, self.get_generic, self.post_n_largest),
            "2" : (self.setup_clamp, self.get_clamp, self.post_clamp),
            "3" : (self.setup_snakespeare, self.get_generic, self.post_snakespeare),
            "999" : (self.setup_dummy, self.get_generic, self.post_dummy)
        }[id]
        self.use_numpy = use_numpy
        self.args = setup(**kwargs)
        self.shuffle_func = {
            False : random.shuffle,
            True : np.random.shuffle
        }[use_numpy]
        
    # 1 - N largest numbers
    def setup_n_largest(self, length=10000, n=50):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(length)
        else:
            lst = list(range(length))
        return (lst, n)
    
    def post_n_largest(self, results):
        return results
        
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
    
    def post_clamp(self, results):
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
            C_TEXT = '\033[91m'
        else:
            C_TEXT = '\033[92m'
        C_END = '\033[0m'
        string = "{}Matrix does {}contain numbers < 0 or > 255.{}".format(
            C_TEXT,
            {True : "still ", False : "not "}[contains],
            C_END
        )
        return string
            
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        with open("./data/sonnets.txt", "r") as fp:
            sonnets = fp.read()
        if self.use_numpy:
            sonnets = np.array(sonnets)
        return (sonnets,)

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
    
    # 999 - Dummy exercise
    def setup_dummy(self):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(10000)
        else:
            lst = list(range(10000))
        n = 100
        return (lst, n)
    
    def post_dummy(self, result):
        pass
        
    # Argument getter
    def get_generic(self):
        if self.shuffle:
            self.shuffle_func(self.args[0])
        return self.args


class TestRunHandler(SolutionHandler):
    def setup_n_largest(self):
        return super().setup_n_largest(length=10, n=3)
    
    def setup_clamp(self):
        return super().setup_clamp(size=4)
    
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