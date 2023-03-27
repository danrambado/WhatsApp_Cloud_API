import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { Button, DatePicker } from 'antd';
import Sidebar from '../components/Sidebar';
import _ from 'lodash';
import moment from 'moment';
import dayjs from 'dayjs';


interface TableDataItem {
  date_only: string;
  time_only: string;
  last_name: string;
  first_name: string;
  status: string;
}

const TablePage = () => {
  const [tableData, setTableData] = useState<TableDataItem[]>([]);
  const [sortBy, setSortBy] = useState<keyof TableDataItem>('time_only');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');
  const [selectedDate, setSelectedDate] = useState<dayjs.Dayjs | null>(null);

  const handleDateChange = (date: dayjs.Dayjs | null) => {
    setSelectedDate(date);
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const queryParams = selectedDate ? `?date=${selectedDate.format('YYYY-MM-DD')}` : '';
        const response = await fetch(`http://192.168.1.5:8000/get_appointments${queryParams}`);
        const data = await response.json();
        console.log('Data fetched:', data);
        setTableData(data.map((item: any) => ({
          date_only: item.date_only,
          time_only: item.time_only,
          last_name: item.last_name,
          first_name: item.first_name,
          status: item.status
        })));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
    const intervalId = setInterval(() => {
      fetchData();
    }, 30000);

    return () => clearInterval(intervalId);
  }, [selectedDate]);

  const sortedData = _.orderBy(tableData, [sortBy], [sortOrder]);

  const handleClick = () => {
    if (sortOrder === 'asc') {
      setSortOrder('desc');
    } else {
      setSortOrder('asc');
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-r from-blue-500 via-iafpink to-blue-500 animate-gradient-move">
      <Sidebar />

      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-6 text-white">Confirmaciones</h1>
        <Link href="/">
        <Button type="primary" className="bg-white text-iafpink">Ir al Menu</Button>
        </Link>
        <div className="my-4">
        <DatePicker onChange={handleDateChange} />
        </div>

        <div className="bg-white p-4 rounded-md shadow-md mt-4">
          <table className="w-full">
            <thead>
              <tr>
              <th className="border px-4 py-2" onClick={handleClick}>
                Fecha
              </th>
              <th className="border px-4 py-2" onClick={handleClick}>
                  Hora
              </th>
              <th className="border px-4 py-2" onClick={handleClick}>
                    Nombre
              </th>
              <th className="border px-4 py-2" onClick={handleClick}>
                  Apellido
              </th>
              <th className="border px-4 py-2" onClick={handleClick}>
                Estado
              </th>
              </tr>
            </thead>
            <tbody>
              {sortedData.map((row, index) => (
                <tr key={index} className={`${index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}`}>
                  <td className="border px-4 py-2">{row.date_only}</td>
                  <td className="border px-4 py-2">{row.time_only}</td>
                  <td className="border px-4 py-2">{row.first_name}</td>
                  <td className="border px-4 py-2">{row.last_name}</td>
                  <td className="border px-4 py-2">{row.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="mt-4"></div>
        </div>
      </div>
    </div>
  );
};

export default TablePage;
