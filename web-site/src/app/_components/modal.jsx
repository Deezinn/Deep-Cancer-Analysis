'use client';
import React from "react";
import Image from "next/image";
import { ultrasoundImages } from "../_constants/ultra_images";

export const Modal = ({ context, onClose }) => {

    const renderContent = () => {
        switch (context) {
            case "iaTumores":
                return (
                    <div className="flex flex-col gap-4">
                        <h2 className="text-2xl font-bold text-blue-600">Ferramenta de IA - Tumores Cerebrais</h2>
                        <p className="text-gray-700">
                            Esta ferramenta utiliza inteligência artificial para responder suas dúvidas sobre tumores cerebrais.
                            Você pode descrever sintomas ou informações e receber explicações baseadas em dados médicos.
                        </p>
                    </div>
                );
            case "ultrassonografia":
                return (
                    <div className="flex flex-col gap-4">
                        <h2 className="text-2xl font-bold text-blue-600">Instruções - Análise de Imagem</h2>
                        <p className="text-gray-700">
                            Você pode inserir imagens de ultrassonografia cerebral. A ferramenta irá analisar a imagem e informar a probabilidade de presença de câncer.
                        </p>

                        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-3">
                            {ultrasoundImages.map((img, idx) => (
                                <div
                                    key={idx}
                                    className="border rounded-xl overflow-hidden shadow hover:shadow-lg transition duration-200 relative w-full h-40"
                                >
                                    <Image
                                        src={img}
                                        alt={`Ultrassonografia ${idx + 1}`}
                                        fill
                                        className="object-fill"
                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                );
            default:
                return <p className="text-gray-500">Contexto desconhecido</p>;
        }
    };

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 px-4 backdrop-blur-sm transition-opacity duration-200">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-5xl max-h-[80vh] overflow-y-auto p-6 flex flex-col animate-fadeIn mt-30 md:mt-0">
                {renderContent()}
                <div className="flex justify-end mt-6">
                    <button
                        onClick={onClose}
                        className="bg-blue-500 text-white px-5 py-2 rounded-xl font-semibold hover:bg-blue-600 transition"
                    >
                        Fechar
                    </button>
                </div>
            </div>
        </div>
    );
};
