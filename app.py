import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
## Function To get response from LLAma 2 model

def get_llama_response(inputt,no_of_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {inputt}
        within {no_of_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","inputt",'no_of_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs", page_icon='🦜',
                   layout='centered', initial_sidebar_state='collapsed')

# Set the heading for the app
st.header("Start Generating Blogs 🦜")

# Input field for the blog topic
inputt = st.text_input("Enter the Blog topic")


#additional two columns
col1, col2=st.columns([5,5])
with col1:
    no_of_words=st.text_input("Number of Words")
with col2:
    blog_style=st.selectbox("Writing the blog for",('Data Scientist', 'Researchers', 'Common People'),index=0)
submit=st.button("Generate")

## Final response
if submit:
    st.write(get_llama_response(inputt,no_of_words,blog_style))