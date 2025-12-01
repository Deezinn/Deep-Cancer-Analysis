'use client';

import { useState, useRef, useEffect } from "react";
import { options } from "./_constants/inputs";
import { helpsCards } from "./_constants/helps";
import { Modal } from "@/app/_components/modal";
import { teste } from "@/app/_service/llm";
import { IAResponse } from "./_components/ia";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [value, setValue] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const [showModal, setShowModal] = useState(false);
  const [modalContext, setModalContext] = useState("");

  const fileInputRef = useRef(null);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleFileChange = (e) => setFile(e.target.files?.[0] || null);
  const handleClick = () => fileInputRef.current?.click();

  const handleSend = async () => {
    if (!value.trim() && !file) return;

    setMessages((prev) => [
      ...prev,
      { role: "user", content: value, image: file ? URL.createObjectURL(file) : null },
    ]);

    try {
      setLoading(true);
      const response = await teste({ text: value, file });

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: <IAResponse data={response} /> },
      ]);

      setValue("");
      setFile(null);
      if (fileInputRef.current) fileInputRef.current.value = "";

    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const openModal = (context) => {
    setModalContext(context);
    setShowModal(true);
  };

  const closeModal = () => {
    setModalContext("");
    setShowModal(false);
  };

  const isEmpty = messages.length === 0;

  return (
    <div className="flex flex-col min-h-screen bg-blue-50 relative">

      {/* Título */}
      {isEmpty && (
        <section className="w-full text-center mt-45 md:mt-72 px-4">
          <h1 className="text-4xl md:text-5xl font-semibold">
            Entenda seus <span className="text-blue-500">exames</span> com a nossa <span className="font-bold">IA</span>
          </h1>
        </section>
      )}

      {/* Chat */}
      <main className={`flex-1 overflow-y-auto px-4 md:px-0 flex flex-col gap-4 mt-6`}>
        <div className="max-w-3xl mx-auto flex flex-col gap-4 mt-30">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`w-full p-4 rounded-2xl shadow-md ${msg.role === "assistant" ? "bg-white" : "bg-blue-100"} break-words`}
            >
              {msg.image && (
                <img src={msg.image} alt="upload" className="w-32 h-32 rounded mb-3 object-cover" />
              )}
              {typeof msg.content === "string" ? (
                <p className="whitespace-pre-wrap">{msg.content}</p>
              ) : (
                msg.content
              )}
            </div>
          ))}
          <div ref={bottomRef}></div>
        </div>

        {/* Help Cards */}
        {isEmpty && (
          <section className="w-full max-w-xl mx-auto mt-8 flex flex-col gap-2 px-4">
            {helpsCards.map((card, idx) => (
              <div
                key={idx}
                onClick={() =>
                  openModal(card.label === "Ajuda com imagem" ? "ultrassonografia" : "iaTumores")
                }
                className="w-full bg-white hover:shadow-xl transition duration-150 rounded-xl flex justify-between items-center px-4 py-3 text-gray-600 cursor-pointer"
              >
                <div className="flex items-center gap-2">{card.icon} {card.label}</div>
                {card.arrow}
              </div>
            ))}
          </section>
        )}
      </main>

      {/* Input fixo */}
      <footer className="w-full p-4">
        <div className="max-w-3xl mx-auto flex flex-col bg-white rounded-2xl shadow-lg p-4 gap-3">

          <input
            type="text"
            placeholder="Envie uma mensagem..."
            className="w-full h-12 border border-gray-300 rounded-xl px-4 outline-none focus:ring-2 focus:ring-blue-400"
            value={value}
            onChange={(e) => setValue(e.target.value)}
          />

          <div className="flex items-center gap-3">
            {!file && options.map((option, idx) => (
              <div
                key={idx}
                onClick={handleClick}
                className="shadow rounded-full bg-gray-200 p-2 cursor-pointer hover:bg-gray-300 transition"
              >
                {option.icon}
              </div>
            ))}

            {file && (
              <div className="flex items-center gap-4">
                <img src={URL.createObjectURL(file)} className="w-20 h-20 object-cover rounded" />
                <button
                  className="text-red-500 text-sm font-semibold"
                  onClick={() => { setFile(null); fileInputRef.current.value = ""; }}
                >
                  Remover
                </button>
              </div>
            )}

            <input
              type="file"
              accept="image/*"
              ref={fileInputRef}
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
          </div>

          <button
            onClick={handleSend}
            disabled={loading}
            className={`w-full py-3 rounded-xl text-white font-bold transition ${loading ? "bg-blue-300 cursor-not-allowed" : "bg-blue-500 hover:bg-blue-600"}`}
          >
            {loading ? "Enviando..." : "Enviar"}
          </button>
        </div>
      </footer>

      {showModal && <Modal context={modalContext} onClose={closeModal} />}
    </div>
  );
}
