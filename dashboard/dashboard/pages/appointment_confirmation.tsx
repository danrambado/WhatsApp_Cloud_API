import React, { useEffect, useState } from 'react';
import Sidebar from '../components/Sidebar';

interface TableDataItem {
    fecha: string;
    nombre: string;
  }

const TablePage = () => {
    const [tableData, setTableData] = useState<TableDataItem[]>([]);

  useEffect(() => {
    const fetchData = async () => {
        try {
          const response = await fetch('http://host.docker.internal:8000/appointments');
          const data = await response.json();
          console.log('Data fetched:', data);
          setTableData(data); // Cambia esto para asignar directamente la respuesta JSON
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    fetchData();
    const intervalId = setInterval(() => {
      fetchData();
    }, 30000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="min-h-screen w-full bg-gradient-to-r from-blue-500 via-iafpink to-blue-500 animate-gradient-move">
      <Sidebar />
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-6 text-white">Tabla de ejemplo</h1>
        <div className="bg-white p-4 rounded-md shadow-md">
          <table className="w-full">
          <thead>
            <tr>
                <th className="border px-4 py-2">Fecha</th>
                <th className="border px-4 py-2">Nombre</th>
            </tr>
            </thead>
            <tbody>
            {tableData.map((row, index) => (
                <tr key={index} className={`${index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}`}>
                <td className="border px-4 py-2">{row.fecha}</td>
                <td className="border px-4 py-2">{row.nombre}</td>
                </tr>
            ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default TablePage;
