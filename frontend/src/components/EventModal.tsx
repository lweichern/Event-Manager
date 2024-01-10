import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Pencil } from "lucide-react";
import { EventType } from "./EventList";
import { useState } from "react";
import axios from "axios";
import { DialogClose } from "@radix-ui/react-dialog";
import { useEventStore } from "@/lib/stateManagement";

export function EventModal({ event }: { event: EventType }) {
  const fetchEvents = useEventStore((state) => state.fetchEvents);
  const [inputVal, setInputVal] = useState(event.name);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputVal(e.target.value);
  };

  const editEvent = async () => {
    await axios.put(`/api/events/${event.id}`, {
      name: inputVal,
    });
    fetchEvents();
  };
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" className="p-2">
          <Pencil />
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Edit Event</DialogTitle>
          <DialogDescription>
            Make changes to your event here. Click save when you're done.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="name" className="text-right">
              Name
            </Label>
            <Input
              id="name"
              value={inputVal}
              className="col-span-3"
              onChange={handleChange}
              autoComplete="off"
            />
          </div>
        </div>
        <DialogFooter>
          <DialogClose>
            <Button onClick={editEvent}>Save changes</Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
