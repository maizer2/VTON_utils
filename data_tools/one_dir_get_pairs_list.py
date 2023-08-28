import os, random, argparse


class get_pairs_list:
    
    def check_pairs(self,
                    A_list: list,
                    B_list: list):
        A_list.sort(), B_list.sort()
        
        if len(A_list) != len(B_list):
            raise Exception("Two list aren't match length")
        
        for idx, a in enumerate(A_list):
            if a.split("_")[0] != B_list[idx].split("_")[0]:
                raise Exception("Each data isn't match")
            
        return A_list, B_list
    
    
    def split_files(self, 
                    data_list: list, 
                    A_format: str, 
                    B_format: str):
        
        A_list = []
        B_list = []
        
        for data in data_list:
            if A_format in data:
                A_list.append(data)
            elif B_format in data:
                B_list.append(data)
            else:
                raise ValueError
        
        return self.check_pairs(A_list, B_list)
    
    
    def __init__(self, 
                 data_path: str,
                 A_format: str = "_0",
                 B_format: str = "_1"):
        
        self.A_list, self.B_list = self.split_files(os.listdir(data_path), A_format, B_format)
        
        
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
            txt = self.write_pairs(img_list, cloth_list)
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
    parser.add_argument("--data_path")
    parser.add_argument("--A_format", default="_0")
    parser.add_argument("--B_format", default="_1")
    parser.add_argument("--out_path", default=None)
    parser.add_argument("--no_pairs", action="store_true")
    parser.add_argument("--phase", default="train")
    opt = parser.parse_args()
    
    return opt


if __name__ == "__main__":
    opt = get_opt()
    
    get_pairs_list(opt.data_path)(opt.out_path, opt.no_pairs, opt.phase)
