import Image from "next/image";
import { options } from "./_constants/inputs";
import { helpsCards } from "./_constants/helps";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center font-sans bg-blue-50">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-center gap-5">
        <section className="w-full flex flex-col justify-center items-center gap-10">
          <h1 className="text-5xl text-start">Tire suas <span className="font-bold">dúvidas</span> com nosso especialista médico</h1>
          <div className="w-full h-50 flex flex-col justify-between bg-white rounded-3xl shadow-2xl px-5">
            <input
              type="text"
              placeholder="O que você está pensando?"
              className="w-full h-1/2 focus:outline-none focus:ring-0 focus:border-none border-none"
            />
            <div className="w-full h-auto flex justify-between items-center pb-5">
              {options.map((value, idx) => (
                <div key={idx}>
                  {/* Adicionar as opções de inputs */}
                </div>
              ))}
            </div>
          </div>
        </section>
        <section className="w-full flex flex-col justify-center items-center gap-2">
          {/* Aplicar mapp depois, usar o diretorio constant/helps */}
          {helpsCards.map((value, idx) => {
            return (
              <div className="w-full h-15 hover:shadow-2xl rounded-xl flex justify-between gap-2 items-center px-2 " key={idx}>
                <div className="flex flex-row justify-center items-center gap-2">
                  {value.icon}
                  <h1>{value.label}</h1>
                </div>
                <div className="flex flex-row justify-center items-center">
                  {value.arrow}
                </div>
              </div>
            )
          })}

        </section>
      </main>
    </div>
  );
}
