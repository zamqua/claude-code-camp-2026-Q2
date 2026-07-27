require_relative "tool"
require_relative "message"

module Boukensha

  # Holds everything BOUKENSHA needs to make an API call. Nothing lives outside of this.

  # system: Tells the agent what its job is. Sent as a separate field in the API call,
  #         never inside the messages array.
  # messages: The full conversation history, replayed on every turn
  # tools: The registered tools the agent is allowed to invoke
  # token_budget: How many tokens the run is allowed to consume
  #
  # A basic context needs no description — the system prompt is enough:
  #<Context turns=2 tools=1 budget=8192>
  #
  # When you have multiple tools and a longer-running task, description helps the agent distinguish between them:
  # <Context turns=8 tools=4 budget=8192>
  # system: "You are a MUD player assistant. Use the tools available to you to help the player explore, fight, and interact with the world."
  # tools:  move, attack, look, say
  #
  # A context near its token budget — description matters so the agent can prioritise:
  # <Context turns=24 tools=2 budget=8192 used=7800>
  # system: "You are a MUD combat assistant. Focus on survival — flee if health is low."
  # tools:  attack, move

  # TODO: Should not we name 'system' as 'system_prompt'?
  # TODO: Calling player as 'task' is confusing. Can we call it the object Play instead of Player?

  class Context
    attr_reader :task, :system, :messages, :tools

    def initialize(task:, system: nil)
      @task         = task
      @system       = system
      @messages     = []
      @tools        = {}
    end

    def register_tool(tool)
      @tools[tool.name] = tool
    end

    def add_message(role, content, tool_use_id: nil)
      @messages << Message.new(role, content, tool_use_id)
    end

    def tool_count = @tools.size
    def turn_count = @messages.size

    def to_s
      "#<Context task=#{task&.task_name} turns=#{turn_count} tools=#{tool_count}>"
    end
  end
end
