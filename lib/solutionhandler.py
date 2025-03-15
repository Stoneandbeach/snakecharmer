import random

class SolutionHandler:
    def __init__(self, id, *pargs, **kwargs):
        setup, self.get_args, self.post_process = {
            "1" : (self.setup_n_largest, self.get_generic, self.post_n_largest),
            "2" : (self.setup_clamp, self.get_clamp, self.post_clamp),
            "3" : (self.setup_snakespeare, self.get_generic, self.post_snakespeare),
            "999" : (self.setup_dummy, self.get_generic, self.post_dummy)
        }[id]
        self.args = setup()
        
    # 1 - N largest numbers
    def setup_n_largest(self, length=1000, n=10):
        self.shuffle = True
        lst = sorted(list(range(length)))
        return (lst, n)
    
    def post_n_largest(self, results):
        return results
        
    # 2 - Clamp values
    def setup_clamp(self, size=50):
        self.shuffle = False
        return ([[random.randint(-200, 500) for _ in range(size)] for _ in range(size)],)
    
    def get_clamp(self):
        _matrix = self.args[0]
        return ([row.copy() for row in _matrix],)
    
    def post_clamp(self, results):
        return results
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        with open("./data/sonnets.txt", "r") as fp:
            sonnets = fp.read()
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
        lst = list(range(10000))
        n = 100
        return (lst, n)
    
    def post_dummy(self):
        pass
        
    # Argument getter
    def get_generic(self):
        if self.shuffle:
            random.shuffle(self.args[0])
        return self.args


class TestRunHandler(SolutionHandler):
    def setup_n_largest(self):
        return super().setup_n_largest(length=10, n=3)
    
    def setup_clamp(self):
        return super().setup_clamp(size=4)
    
    def setup_snakespeare(self):
        self.shuffle = False
        sample = 'This text is an example text. This text will hopefully help. For an example is an aid.'
        return (sample,)
    
    def post_snakespeare(self, word_dict):
        print("Word dictionary:")
        for key in word_dict:
            print(key, word_dict[key])
        print()
        return super().post_snakespeare(word_dict)