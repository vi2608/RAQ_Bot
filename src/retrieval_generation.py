from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from src.data_ingestion import ingestdata
from src.prompt import *

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template(WINDOW_BOT_TEMPLATE)

    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__=='__main__':
    vstore = ingestdata("None")
    chain  = generation(vstore)
    print(chain.invoke("Give info about windows?"))
    