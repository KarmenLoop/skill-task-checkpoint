"""Reconstruct interrupted work without blindly repeating uncertain actions."""
from runtime import *

import hashlib
def process(data):
    task=text(data["task_id"],"task_id")
    goal=text(data["goal"],"goal")
    events=records(data,"events")
    states={}
    previous=0
    for event in events:
        seq=integer(event.get("seq"),"seq",1)
        if seq<=previous: raise ValueError("events must have strictly increasing seq")
        previous=seq
        ident=text(event.get("action_id"),"action_id")
        state=choice(event.get("state"),("planned","dispatched","completed","failed","cancelled"),"state")
        current=states.get(ident)
        allowed={"planned":{"dispatched","cancelled"},"dispatched":{"completed","failed","cancelled"}}
        if current is None:
            if state!="planned": raise ValueError("action must begin as planned")
            if type(event.get("replay_safe")) is not bool: raise ValueError("replay_safe must be boolean")
            current={"action_id":ident,"replay_safe":event["replay_safe"]}
        elif state not in allowed.get(current["state"],set()):
            raise ValueError("invalid action transition")
        was_dispatched=current.get("state")=="dispatched"
        current=dict(current,state=state,last_seq=seq)
        if state=="cancelled" and was_dispatched: current["outcome_unknown"]=True
        if state=="completed": current["receipt"]=text(event.get("receipt"),"receipt")
        states[ident]=current
    actions=list(states.values())
    queue=[]
    for action in actions:
        state=action["state"]
        next_step="verify_external_outcome" if action.get("outcome_unknown") else "execute_when_authorized" if state=="planned" else "retry_when_authorized" if state=="dispatched" and action["replay_safe"] else "verify_external_outcome" if state=="dispatched" else "inspect_failure" if state=="failed" else None
        if next_step: queue.append({"action_id":action["action_id"],"next_step":next_step})
    result={"task_id":task,"goal":goal,"actions":actions,"resume_queue":queue}
    result["sha256"]=hashlib.sha256(json.dumps(result,sort_keys=True).encode()).hexdigest()
    return result

if __name__ == "__main__":
    sys.exit(main(process, "Reconstruct interrupted work without blindly repeating uncertain actions."))
