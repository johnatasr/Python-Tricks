#  pip install fastcore


import sys
from fastcore.transform import Pipeline
from pipeline_functions import remove_spaces, remove_special_chars, lowercase


def static_functions_pipeline(input_string):
    # Creates a pipeline with a list of functions
    pipe = Pipeline([remove_spaces, remove_special_chars, lowercase])
    
    # Invokes pipeline
    output = pipe(input_string)

    print(f"""output ==> {output}""")


def dynamic_functions_pipeline(input_string, pipe_funcs):
    # Creates a pipeline with a list of functions using using globals()
    pipe = Pipeline([globals()[func] for func in pipe_funcs])

    # Invokes pipeline
    output = pipe(input_string)

    print(f"""output ==> {output}""")
      

if __name__ == '__main__':
    text = input("Enter input string: ")
    static_functions_pipeline(text)
    
    funcs = sys.argv[1:]

    dynamic_functions_pipeline(text, funcs)