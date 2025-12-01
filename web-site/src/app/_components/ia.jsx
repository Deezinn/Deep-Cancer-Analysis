export const IAResponse = ({ data }) => {
    return (
        <div className="w-full bg-white p-6 rounded-2xl shadow-lg flex flex-col gap-6 mt-4">

            {/* Cabeçalho */}
            <div className="border-b pb-3">
                <h2 className="text-2xl font-bold text-blue-600">Resultado da Análise</h2>
                <p className="text-sm text-gray-500">Relatório gerado pela IA</p>
            </div>

            {/* Probabilidades */}
            <div className="bg-blue-50 p-4 rounded-xl shadow-inner">
                <h3 className="font-semibold text-lg mb-2">Probabilidade de Tumor</h3>
                <p><strong>Score:</strong> {data.probabilidade_tumor?.toFixed(5)}</p>
                <p><strong>Percentual:</strong> {data.probabilidade_tumor_percent ?? "N/A"}%</p>
                <p><strong>Classificação:</strong> {data.classificacao_modelo ?? "Não disponível"}</p>
                <p>
                    <strong>Modelo indica tumor:</strong>{" "}
                    {data.modelo_indica_tumor !== undefined ? (
                        data.modelo_indica_tumor ? (
                            <span className="text-red-600 font-bold">Sim</span>
                        ) : (
                            <span className="text-green-600 font-bold">Não</span>
                        )
                    ) : (
                        <span className="text-gray-500 font-semibold">Indefinido</span>
                    )}
                </p>
            </div>

            {/* Relatório LLM */}
            <div className="bg-gray-50 p-4 rounded-xl whitespace-pre-wrap leading-relaxed text-gray-700">
                <h3 className="font-semibold text-lg mb-2">Relatório Clínico</h3>
                {data.relatorio_llm ? (
                    data.relatorio_llm
                ) : (
                    <p className="text-gray-500 italic">Nenhum relatório clínico gerado pela IA.</p>
                )}
            </div>
        </div>
    );
};
