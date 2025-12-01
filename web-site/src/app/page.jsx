'use client'
import Image from "next/image";
import { options } from "./_constants/inputs";
import { helpsCards } from "./_constants/helps";
import { useEffect, useState, useRef } from "react";

export default function Home() {
  const [value, setValue] = useState("");
  const [file, setFile] = useState(null); 
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0] || null; 
    setFile(selectedFile);
  };

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleSend = () => {
    console.log("Enviando texto:", value);
    if (file) console.log("Enviando arquivo:", file);

    setValue("");
    setFile('');
  };

  useEffect(() => {
    console.log("Texto atual:", value);
  }, [value]);

  return (
    <div className="flex min-h-screen items-center justify-center font-sans bg-blue-50">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-center gap-5 px-4 md:px-0">
        <section className="w-full flex flex-col justify-center items-center gap-5 md:gap-10">
          <h1 className="text-4xl md:text-5xl text-center md:text-start">
            Entenda seus <span className="text-blue-500">exames</span> com ajuda da nossa <span className="font-bold">IA.</span>
          </h1>
          <div className="w-full flex flex-col justify-between bg-white rounded-3xl shadow-2xl px-5 py-4">
            {/* Input de texto */}
            <input
              type="text"
              placeholder="O que você está pensando?"
              className="w-full h-12 focus:outline-none focus:ring-0 focus:border-none border-none mb-3"
              value={value} // sempre controlado
              onChange={(e) => setValue(e.target.value)}
            />

            {/* Upload de imagem */}
            <div className="w-full flex items-center gap-3 mb-3">
              {!file && (
                <>
                  {options.map((option, idx) => (
                    <div
                      key={idx}
                      onClick={handleClick}
                      className="shadow-2xl rounded-full bg-gray-200 p-1.5 cursor-pointer flex items-center justify-center hover:bg-gray-300"
                    >
                      {option.icon}
                    </div>
                  ))}

                  <input
                    type="file"
                    accept="image/*"
                    ref={fileInputRef}
                    onChange={handleFileChange}
                    style={{ display: "none" }}
                  />
                </>
              )}

              {file && (
                <div className="ml-4">
                  <img
                    src={URL.createObjectURL(file)}
                    alt="preview"
                    className="w-24 h-24 object-cover rounded"
                  />
                </div>
              )}
            </div>

            {/* Botão de enviar (imagem opcional) */}
            <button
              onClick={handleSend}
              className="w-full py-2 rounded-xl text-white font-bold bg-blue-500 hover:bg-blue-600"
            >
              Enviar
            </button>
          </div>
        </section>

        {/* Cards de ajuda */}
        <section className="w-full flex flex-col justify-center items-center gap-2 mt-6">
          {helpsCards.map((value, idx) => (
            <div
              key={idx}
              className="w-full h-15 hover:shadow-2xl duration-150 delay-100 rounded-xl flex justify-between gap-2 items-center px-2 text-gray-500"
            >
              <div className="flex flex-row justify-center items-center gap-2">
                {value.icon}
                <h1>{value.label}</h1>
              </div>
              <div className="flex flex-row justify-center items-center">
                {value.arrow}
              </div>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
}
