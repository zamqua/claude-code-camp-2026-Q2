require_relative "errors"

module Boukensha


  # The Tool Registry is how BOUKENSHA manages what capabilities the agent can use. 
  # It has two jobs: 
  # 1. storing tools
  # 2. dispatching tools when asked

  class Registry
    def initialize(context)
      @context = context
    end

    def tool(name, description:, parameters: {}, &block)
      tool = Tool.new(name.to_s, description, parameters, block)
      @context.register_tool(tool)
      tool
    end

    def dispatch(name, args = {})
      tool = @context.tools[name.to_s]
      raise UnknownToolError, "No tool registered as '#{name}'" unless tool
      tool.block.call(**args.transform_keys(&:to_sym))
    end

  end
end