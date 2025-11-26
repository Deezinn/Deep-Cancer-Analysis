'use client'
import { Icon } from "@iconify/react";
import { useState } from "react";

export const Navbar = () => {

    return (
        <>
            <div className="w-full h-auto flex justify-center items-center fixed top-0 left-0 z-50 p-10 text-blue-500">
                <nav className="w-4/5 h-15 bg-white rounded-full flex items-center justify-between px-5 shadow-2xl">
                    {/* Logo */}
                    <div className="w-full flex flex-row justify-start items-center gap-5">
                        <Icon icon="icon-park-twotone:brain" width={30} height={30} />
                        <h1>Medica<span className="font-bold">AI</span></h1>
                    </div>
                    {/* Equipe */}
                    <div className="w-full h-10 flex flex-row justify-end items-center">
                        <div className="w-auto p-2 flex flex-row justify-end items-center gap-5 rounded-xl bg-gray-100 cursor-pointer">
                            <h1>Equipe</h1>
                            <Icon icon="zondicons:user-group" width={20} height={20} />
                        </div>
                    </div>
                </nav>
            </div>
        </>
    );
};
