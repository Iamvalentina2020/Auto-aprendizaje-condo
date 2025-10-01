import { useEffect } from 'react';
import './Notification.css';

export default function Notification({ message, type, onClose }) {
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => {
        onClose();
      }, 4000);
      return () => clearTimeout(timer);
    }
  }, [message, onClose]);

  if (!message) return null;

  return (
    <div className={`notification glass ${type}`}>
      <span className="notification-icon">
        {type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️'}
      </span>
      <span className="notification-message">{message}</span>
      <button className="notification-close" onClick={onClose}>
        ✕
      </button>
    </div>
  );
}
