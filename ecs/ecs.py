from itertools import count
from typing import Type, Any
from .component import Component
from .system import System

class ECS:
    def __init__(self):
        self.entities: dict[int:dict] = {}
        self.systems: list[System] = []
        self.entity_count: count = count(start=1)
        self.globals: dict[str:Any] = {}

    def create_entity(self, components: list[Component] = []) -> int:
        entity_id: int = next(self.entity_count)
        entity = {}
        for component_instance in components:
            component_type = type(component_instance)
            entity[component_type] = component_instance
        self.entities[entity_id] = entity
        return entity_id

    def get_entity_component(self, entity_id: int, component_type: Type[Component]) -> Component:
        return self.entities[entity_id][component_type]

    def remove_entity_component(self: int, entity_id, component_type: Type[Component]):
        del self.entities[entity_id][component_type]

    def add_entity_component(self, entity_id: int, component: Component):
        self.entities[entity_id][type(component)] = component
    
    def add_system(self, system: System, priority: int) -> None:
        system.priority = priority
        self.systems.append(system)
        self.systems.sort(key=lambda sys: sys.priority, reverse=True)
    
    def remove_system(self, system_type: Type[System]):
        for system in self.systems:
            if type(system) is system_type:
                self.systems.remove(system)
    
    def get_components(self, required_component_types: list[Type[Component]]) -> list[list[Component]]:
        all_entity_components = []
        for entity in self.entities.values():
            entity_component_types = entity.keys()

            found_components = []
            for required_component_type in required_component_types:
                if required_component_type in entity_component_types:
                    found_components.append(entity[required_component_type])
            
            if len(found_components) == len(required_component_types):
                all_entity_components.append(found_components)
        return all_entity_components
            
    def update_systems(self) -> None:
        for system in self.systems:
            system.update(self)
    
    def add_global(self, name: str, value: Any = None) -> None:
        self.globals[name] = value
    
    def update_global(self, name: str, value: Any) -> None:
        self.globals[name] = value
    
    def get_global(self, name: str) -> Any:
        return self.globals[name]