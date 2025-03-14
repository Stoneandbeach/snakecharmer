import random

class SolutionHandler:
    def __init__(self, id, *pargs, test_mode=False, **kwargs):
        self.test_mode = test_mode
        self.args, self.get_args, self.post_process = {
            "1" : (self.setup_n_largest(), self.get_generic, self.post_n_largest),
            "2" : (self.setup_clamp(), self.get_clamp, self.post_clamp),
            "3" : (self.setup_snakespeare(), self.get_generic, self.post_snakespeare),
            "999" : (self.setup_dummy(), self.get_generic, self.post_dummy)
        }[id]
        
    # 1 - N largest numbers
    def setup_n_largest(self):
        self.shuffle = True
        lst = sorted(list(range(1000)))
        n = 10
        return (lst, n)
    
    def post_n_largest(self, results):
        print(results)
        
    # 2 - Clamp values
    def setup_clamp(self):
        self.shuffle = True
        matrix = [[random.randint(-200, 500) for _ in range(2)] for _ in range(2)]
        return (matrix,)
    
    def get_clamp(self):
        for row in self.args[0]:
            random.shuffle(row)
        random.shuffle(self.args[0])
    
    def post_clamp(self, results):
        print(results)
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        with open("../exercise-test/sonnets.txt", "r") as fp:
            sonnets = fp.read()
        return (sonnets,)

    def post_snakespeare(self, word_dict):
        w1, w2 = random.choice([word_pair for word_pair in list(word_dict.keys()) if word_pair[0][0].isupper()])
        num_words = 2
        print("\n" + " ".join([w1, w2]), end=" ")
        while num_words < 10 or w2[-1] != ".":
            try:
                w1, w2 = w2, random.choice(word_dict[(w1, w2)])
            except IndexError as e:
                print()
                print()
                print(f"Error! {e}")
                print(w1, w2, word_dict[(w1, w2)])
                break
            print(w2, end=" ")
            num_words += 1
        print()
    
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

    # Fetch test output
    def test(self, id):
        return {
            "1" : [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],
            "3" : ""
        }