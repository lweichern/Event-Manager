import "./App.css";
import EventForm from "./components/EventForm";
import EventList from "./components/EventList";

function App() {
  return (
    <>
      <div className="flex flex-col gap-6">
        <h1 className=" text-3xl font-semibold text-white">Event Manager</h1>
        <EventForm />
        <EventList />
      </div>
    </>
  );
}

export default App;
