'use client'
import { Icon } from "@iconify/react";
import { useState } from "react";
import { membros } from "../_constants/membros";
export const Navbar = () => {
    const [showTeam, setShowTeam] = useState(false);


    return (
        <div className="w-full h-auto flex justify-center items-center fixed top-0 left-0 z-50 p-10 text-blue-500">
            <nav className="w-full md:w-4/5 h-15 bg-white rounded-full flex items-center justify-between px-5 shadow-2xl relative">
                <div className="w-full flex flex-row justify-start items-center gap-5">
                    <Icon icon="icon-park-twotone:brain" width={30} height={30} />
                    <h1>Medica<span className="font-bold">AI</span></h1>
                </div>

                <div className="w-full h-10 flex flex-row justify-end items-center relative">
                    <div
                        onClick={() => setShowTeam(!showTeam)}
                        className="w-auto p-2 flex flex-row justify-end items-center gap-2 rounded-xl bg-gray-100 cursor-pointer hover:bg-gray-200 transition"
                    >
                        <h1>Equipe</h1>
                        <Icon icon="zondicons:user-group" width={20} height={20} />
                    </div>
                    {showTeam && (
                        <div className="absolute top-full right-0 mt-5 bg-white rounded-xl shadow-xl p-4 w-56 flex flex-col gap-3 z-50">
                            {membros.map((member, idx) => (
                                <div key={idx} className="flex items-center gap-3">
                                    <img
                                        src={member.image}
                                        alt={member.name}
                                        className="w-10 h-10 rounded-full object-cover border-2 border-blue-500"
                                    />
                                    <h2 className="text-sm font-medium">{member.name}</h2>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </nav>
        </div>
    );
};
