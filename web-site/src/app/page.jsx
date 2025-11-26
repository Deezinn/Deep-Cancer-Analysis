import Image from "next/image";
import { options } from "./_constants/inputs";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center font-sans bg-blue-50 px-10">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-center gap-10 pb-30">
        <h1 className="text-5xl text-start">Tire suas <span className="font-bold">dúvidas</span> com nosso especialista médico</h1>
        <div className="w-full h-50 flex flex-col justify-between bg-white rounded-3xl shadow-2xl px-5">
          <input
            type="text"
            placeholder="O que você está pensando?"
            className="w-full h-1/2 focus:outline-none focus:ring-0 focus:border-none border-none"
          />
          <div className="w-full h-auto flex justify-between items-center pb-5">
            {options.map((value, idx) =>(
              <div key={idx}>
                {/* Adicionar as opções de inputs */}
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
