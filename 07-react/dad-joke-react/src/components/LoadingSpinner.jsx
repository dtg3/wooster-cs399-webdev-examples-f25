function LoadingSpinner() {
  return (
    <div 
      className="spinner-border text-warning" 
      role="status" 
    >
      <span className="visually-hidden">Loading...</span>
    </div>
  );
}

export default LoadingSpinner;