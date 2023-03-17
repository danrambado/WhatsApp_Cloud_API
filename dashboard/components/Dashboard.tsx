import React from 'react';
import styles from '../styles/Dashboard.module.css';



interface Appointment {
  id: number;
  date: string;
  time: string;
  patientName: string;
  doctorId: number;
  patientId: number;
  status: string;
}

const appointments: Appointment[] = [
  {
    id: 1,
    date: '2023-03-20',
    time: '10:00',
    patientName: 'John Doe',
    doctorId: 101,
    patientId: 201,
    status: 'Confirmed',
  },
  {
    id: 2,
    date: '2023-03-20',
    time: '11:00',
    patientName: 'Jane Smith',
    doctorId: 102,
    patientId: 202,
    status: 'Cancelled',
  },
];

const Dashboard: React.FC = () => {
    return (
      <div>
        <h1>Appointment Dashboard</h1>
        <table className={styles.table}>
          <thead className={styles.tableHead}>
            <tr>
              <th className={styles.tableHeader}>ID</th>
              <th className={styles.tableHeader}>Date</th>
              <th className={styles.tableHeader}>Time</th>
              <th className={styles.tableHeader}>Patient Name</th>
              <th className={styles.tableHeader}>Doctor ID</th>
              <th className={styles.tableHeader}>Patient ID</th>
              <th className={styles.tableHeader}>Status</th>
            </tr>
          </thead>
          <tbody>
            {appointments.map((appointment) => (
              <tr className={styles.tableRow} key={appointment.id}>
                <td className={styles.tableCell}>{appointment.id}</td>
                <td className={styles.tableCell}>{appointment.date}</td>
                <td className={styles.tableCell}>{appointment.time}</td>
                <td className={styles.tableCell}>{appointment.patientName}</td>
                <td className={styles.tableCell}>{appointment.doctorId}</td>
                <td className={styles.tableCell}>{appointment.patientId}</td>
                <td className={styles.tableCell}>{appointment.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };

export default Dashboard;

