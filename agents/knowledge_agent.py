from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
import os
def load_documents(faiss_index_path):

    api_key = "sk-IsaJkydPhYtOSR9Qh5aAkYz6Trnh3ow2h7RyAQa950JqmeEn"
    base_url = "https://api.chatanywhere.tech/v1"
    embedding_model = "text-embedding-ada-002"
    index_name = "INDEX"

    """初始化嵌入模型"""
    embeddings = OpenAIEmbeddings(
        api_key=api_key,
        base_url=base_url,
        model=embedding_model
    )
    """初始化向量存储"""
    if not os.path.exists(faiss_index_path):
        raise FileNotFoundError(f"FAISS索引文件不存在: {faiss_index_path}")
    vector_store = FAISS.load_local(
        folder_path=faiss_index_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
        index_name=index_name
    )
    retriever = vector_store.as_retriever()
    return  retriever

def create_knowledge_agent():
    # API配置
    api_key = "sk-IsaJkydPhYtOSR9Qh5aAkYz6Trnh3ow2h7RyAQa950JqmeEn"
    base_url = "https://api.chatanywhere.tech/v1"
    llm_model = "gpt-3.5-turbo"
    temperature = 0

    """3. 初始化 LLM"""
    llm = ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=llm_model,
        temperature=temperature,
    )

    retriever = load_documents(".\\file\\xx")
    """3. 初始化QA问答系统"""
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

"""6. 测试运行"""
if __name__ == "__main__":
    result = create_knowledge_agent()
    result.invoke({"user_input": "c测试qa"})
    print(result)
