
module Boukensha
  # name: The name of the tool
  # description: Shown to the agent so it knows when to invoke the tool
  # parameters: The arguments that need to be passed in
  # block: The actual code that runs when the tool is called
  ## Examples
  # <Tool name=move description="Move the player in a direction (north, south, east, west, up, down)" params=[:direction]>
  # <Tool name=attack description="Attack a target in the current room" params=[:target]>
  # <Tool name=look description="Look around the current room" params=[]>
  # <Tool name=say description="Say something out loud to others in the room" params=[:message]>
  ##
  Tool = Struct.new(:name, :description, :parameters, :block) do
    def to_s
      "#<Tool name=#{name} description=#{description.to_s[0..40]} params=#{parameters.keys}>"
    end
  end
end