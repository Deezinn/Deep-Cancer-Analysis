import { Icon } from "@iconify/react";

export const Navbar = () => {
    return (
        <div className="w-full h-20 grid grid-cols-2">
            <div className="w-full h-full flex justify-start items-center">
                <Icon icon="svg-spinners:gooey-balls-1" width={30} height={30}/>
            </div>
            <div className="w-full h-full flex justify-end items-center">
                <div className="w-1/7 h-auto flex flex-row gap-5 justify-end items-center bg-gray-500 px-2 py-1 rounded-full text-white">
                    <h1>Equipe</h1>
                    <Icon icon="material-symbols:account-circle" width={30} height={30} />
                </div>
            </div>
        </div>
    );
};
