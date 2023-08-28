import os, random, argparse


class get_pairs_list:
            
    def __init__(self, 
                 A_path: str, 
                 B_path: str):
        
        self.A_list = os.listdir(A_path)
        self.B_list = os.listdir(B_path)
        
        
    def write_pairs(self, A: list, B: list) -> str:
        txt = ""
        for idx, item in enumerate(A):
            txt += f"{item} {B[idx]}\n"
        
        return txt
    
    
    def make_pairs_list(self, 
                        out_path: str = None, 
                        no_pairs: bool = False, 
                        pairs_name: str = "train_paired.txt"):
        img_list, cloth_list = self.A_list, self.B_list
        
        if not no_pairs:
            txt = self.write_pairs(img_list, img_list)
        else:
            random.shuffle(cloth_list)
            txt = self.write_pairs(img_list, cloth_list)
        
        if out_path is None:
            out_path = os.path.join("./", pairs_name)
            
        with open(out_path, "w") as f:
            f.write(txt)
            
    
    def __call__(self,
                 out_path: str = None,
                 no_pairs: bool = False,
                 phase: str = "train"):
        
        pairs_name = phase + "_" + ("unpaired" if no_pairs else "paired") + ".txt"
        
        self.make_pairs_list(out_path, no_pairs, pairs_name)


def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--A_path")
    parser.add_argument("--B_path")
    parser.add_argument("--out_path", default=None)
    parser.add_argument("--no_pairs", action="store_true")
    parser.add_argument("--phase", default="train")
    opt = parser.parse_args()
    
    return opt


if __name__ == "__main__":
    opt = get_opt()
    
    make_pairs_list(opt.A_path, opt.B_path)(opt.out_path, opt.no_pairs, opt.phase)
