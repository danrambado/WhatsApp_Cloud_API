import { useState } from "react";
import { MdMenu, MdClose, MdCheckCircle, MdList, MdAccessTime } from "react-icons/md";
import Link from 'next/link';


const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleToggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  const handleCloseSidebar = () => {
    setIsOpen(false);
  };

  return (
    <>
      <button
      className="fixed top-0 left-0 m-4 p-2 bg-white rounded-full shadow-md focus:outline-none z-10 transition duration-300 hover:bg-gray-100"
      onClick={handleToggleSidebar}
      >
        {isOpen ? (
          <MdClose className="h-8 w-8 text-iafpink transition duration-500 hover:text-blue-500" />
        ) : (
          <MdMenu className="h-12 w-12 text-iafpink transition duration-500 hover:text-blue-500" />
        )}
      </button>

      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-10"
          onClick={handleCloseSidebar}
        >
          <div
            className= "bg-white w-64 h-full fixed left-0 top-0 z-20 transition-all duration-300 ease-in-out"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="text-center pt-8">
              <h1 className="text-4xl font-bold mb-6 text-iafpink">Menu</h1>
              <div className="grid grid-cols-1 gap-4">
                < Link href="/appointment_confirmation">
                <button className="group bg-white p-6 rounded-lg shadow-md flex flex-col items-center space-y-4 transition duration-300 hover:bg-gray-100">
                  <MdCheckCircle className="h-8 w-8 text-iafpink transform transition duration-500 group-hover:scale-125 group-hover:text-blue-500" />
                  <span className="text-x font-semibold text-iafpink transition duration-500 group-hover:text-blue-500">
                    Confirmación de turnos
                  </span>
                </button>
                </Link>
                <button className="group bg-white p-6 rounded-lg shadow-md flex flex-col items-center space-y-4 transition duration-300 hover:bg-gray-100">
                  <MdList className="h-8 w-8 text-iafpink transform transition duration-500 group-hover:scale-125 group-hover:text-blue-500" />
                  <span className="text-x font-semibold text-iafpink transition duration-500 group-hover:text-blue-500">Cuestionarios</span>
                </button>
                <button className="group bg-white p-6 rounded-lg shadow-md flex flex-col items-center space-y-4 transition duration-300 hover:bg-gray-100">
                  <MdAccessTime className="h-8 w-8 text-iafpink transform transition duration-500 group-hover:scale-125 group-hover:text-blue-500" />
                  <span className="text-x font-semibold text-iafpink transition duration-500 group-hover:text-blue-500">Lista de espera</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Sidebar;