import { Link } from "react-router-dom";
import { EventType } from "./EventList";
import { EventModal } from "./EventModal";
import { Check, Trash } from "lucide-react";
import { Button } from "./ui/button";
import axios from "axios";
import { useEventStore } from "@/lib/stateManagement";

function Event({ event }: { event: EventType }) {
  const fetchEvents = useEventStore((state) => state.fetchEvents);
  const deleteEvent = async () => {
    await axios.delete(`/api/events/${event.id}`);
    fetchEvents();
  };

  const tasksUndone = event.tasks.filter((task) => {
    return !task.isDone;
  });

  console.log("count: ", tasksUndone.length);
  return (
    <div className=" bg-slate-900 rounded-md hover:bg-slate-950 flex gap-3 justify-center items-center p-4">
      <Link to={`events/${event.id}`} className="flex gap-3 flex-1 ">
        <h3 className="text-2xl text-white">{event.name}</h3>

        <p
          className={`${
            tasksUndone.length !== 0 ? "bg-red-600" : "bg-green-600"
          } w-8 aspect-square rounded-full flex justify-center items-center text-md text-white`}
        >
          {tasksUndone.length !== 0 ? tasksUndone.length : <Check />}
        </p>
      </Link>
      <EventModal event={event} />
      <Button className="bg-red-600 p-2 hover:bg-red-700" onClick={deleteEvent}>
        <Trash />
      </Button>
    </div>
  );
}

export default Event;
